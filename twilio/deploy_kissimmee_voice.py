# -*- coding: utf-8 -*-
"""Create and deploy the kissimmee-voice Twilio Serverless service.

Mirrors the ocoee-voice and windermere-voice services already on the account:

  caller dials (689) 263-6255
    -> /incoming   screens robocalls: "press any key to be connected"
    -> dials FORWARD_TO with a whisper on the owner's leg
    -> /whisper    "New lead from Kissimmee Concrete. Press any key to accept."
    -> /accept     empty TwiML bridges the two legs
    -> /voicemail  if nobody accepts: recorded message with transcription

Credentials come from the environment, never from this file:
  TWILIO_SID, TWILIO_TOKEN
"""
import base64
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import uuid

SID = os.environ["TWILIO_SID"]
TOK = os.environ["TWILIO_TOKEN"]
AUTH = "Basic " + base64.b64encode(f"{SID}:{TOK}".encode()).decode()

BRAND = "Kissimmee Concrete"
UNIQUE = "kissimmee-voice"
FRIENDLY = "Kissimmee Concrete Call Flow"
NUMBER = "+16892636255"
FORWARD_TO = "+16892427487"
DEPENDENCIES = [
    {"name": "util", "version": "0.12.5"},
    {"name": "@twilio/runtime-handler", "version": "2.1.2"},
    {"name": "xmldom", "version": "0.6.0"},
    {"name": "lodash", "version": "4.17.21"},
    {"name": "twilio", "version": "5.0.3"},
]

FUNCTIONS = {
    "/incoming": '''exports.handler = function (context, event, callback) {
  const twiml = new Twilio.twiml.VoiceResponse();

  if (event.Digits) {
    // Caller pressed a key -> proceed with the normal dial flow.
    twiml.say(
      { voice: 'Polly.Matthew-Neural' },
      'One moment while we connect you.'
    );
    const callerId = /^\\+\\d+$/.test(event.From) ? event.From : context.TWILIO_NUMBER;
    const dial = twiml.dial({
      callerId,
      timeout: 20,
      record: 'record-from-answer-dual',
      action: '/voicemail',
      method: 'POST',
    });
    dial.number({ url: '/whisper', method: 'POST' }, context.FORWARD_TO);
    return callback(null, twiml);
  }

  // First hit: screen out robocalls before ringing the owner. Repeat the
  // prompt once, slowed down, so a real caller has more time to react.
  const gather = twiml.gather({ numDigits: 1, timeout: 8, action: '/incoming', method: 'POST' });
  const s1 = gather.say({ voice: 'Polly.Matthew-Neural' });
  s1.prosody({ rate: '85%' }, 'Thanks for calling Kissimmee Concrete. Press any key to be connected.');
  gather.pause({ length: 1 });
  const s2 = gather.say({ voice: 'Polly.Matthew-Neural' });
  s2.prosody({ rate: '85%' }, 'Thanks for calling Kissimmee Concrete. Press any key to be connected.');
  twiml.hangup();
  return callback(null, twiml);
};
''',
    "/whisper": '''exports.handler = function (context, event, callback) {
  const twiml = new Twilio.twiml.VoiceResponse();
  const gather = twiml.gather({
    numDigits: 1,
    timeout: 5,
    action: '/accept',
    method: 'POST',
  });
  // Opening pause: mobile audio takes about 2 seconds to open after answering (VoLTE).
  gather.pause({ length: 2 });
  const s1 = gather.say({ voice: 'Polly.Matthew-Neural' });
  s1.prosody({ rate: '85%' }, 'New lead from Kissimmee Concrete. Press any key to accept.');
  gather.pause({ length: 1 });
  const s2 = gather.say({ voice: 'Polly.Matthew-Neural' });
  s2.prosody({ rate: '85%' }, 'New lead from Kissimmee Concrete. Press any key to accept.');
  // No keypress: hang up this leg so the caller is sent to voicemail.
  twiml.hangup();
  return callback(null, twiml);
};
''',
    "/accept": '''exports.handler = function (context, event, callback) {
  // Empty TwiML ends call screening and bridges the two legs.
  const twiml = new Twilio.twiml.VoiceResponse();
  return callback(null, twiml);
};
''',
    "/voicemail": '''exports.handler = function (context, event, callback) {
  const twiml = new Twilio.twiml.VoiceResponse();

  // Re-entry after <Record> finishes.
  if (event.RecordingSid) {
    twiml.say({ voice: 'Polly.Matthew-Neural' }, 'Thank you. We will call you back shortly. Goodbye.');
    twiml.hangup();
    return callback(null, twiml);
  }

  // Call was actually bridged and has ended normally.
  if (event.DialBridged === 'true' || event.DialBridged === true) {
    twiml.hangup();
    return callback(null, twiml);
  }

  // Missed / rejected by screening / busy / failed -> voicemail.
  twiml.say(
    { voice: 'Polly.Matthew-Neural' },
    'Sorry we missed your call. Please leave your name, phone number, and a few details about your project after the beep, and we will get back to you as soon as possible.'
  );
  twiml.record({ maxLength: 120, timeout: 5, playBeep: true, transcribe: true });
  twiml.say({ voice: 'Polly.Matthew-Neural' }, 'Thank you. Goodbye.');
  return callback(null, twiml);
};
''',
}


def req(method, url, data=None, headers=None, form=True):
    h = {"Authorization": AUTH}
    body = None
    if data is not None:
        if form:
            body = urllib.parse.urlencode(data, doseq=True).encode()
            h["Content-Type"] = "application/x-www-form-urlencoded"
        else:
            body = data
    if headers:
        h.update(headers)
    r = urllib.request.Request(url, data=body, method=method, headers=h)
    try:
        return json.loads(urllib.request.urlopen(r, timeout=120).read())
    except urllib.error.HTTPError as e:
        payload = e.read().decode()
        raise SystemExit("HTTP %s on %s %s\n%s" % (e.code, method, url, payload[:600]))


def upload_version(service_sid, function_sid, path, content):
    """Function versions are uploaded as multipart to serverless-upload.twilio.com."""
    boundary = "----" + uuid.uuid4().hex
    parts = []
    for key, val in (("Path", path), ("Visibility", "protected")):
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{key}\"\r\n\r\n{val}\r\n")
    parts.append(
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"Content\"; filename=\"handler.js\"\r\n"
        f"Content-Type: application/javascript\r\n\r\n{content}\r\n"
    )
    parts.append(f"--{boundary}--\r\n")
    body = "".join(parts).encode("utf-8")
    url = f"https://serverless-upload.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions"
    return req("POST", url, body, headers={"Content-Type": "multipart/form-data; boundary=" + boundary}, form=False)


def main():
    base = "https://serverless.twilio.com/v1/Services"

    # 1. service (idempotent: reuse if the unique name already exists)
    existing = req("GET", base + "?PageSize=50").get("services", [])
    svc = next((s for s in existing if s["unique_name"] == UNIQUE), None)
    if svc:
        print("1. service exists:", svc["sid"])
    else:
        svc = req("POST", base, {"UniqueName": UNIQUE, "FriendlyName": FRIENDLY,
                                 "IncludeCredentials": "true", "UiEditable": "false"})
        print("1. service created:", svc["sid"])
    ssid = svc["sid"]

    # 2. functions + versions
    have = {f["friendly_name"]: f for f in req("GET", f"{base}/{ssid}/Functions?PageSize=50").get("functions", [])}
    versions = []
    for path, content in FUNCTIONS.items():
        name = path.strip("/")
        fn = have.get(name) or req("POST", f"{base}/{ssid}/Functions", {"FriendlyName": name})
        ver = upload_version(ssid, fn["sid"], path, content)
        versions.append(ver["sid"])
        print("2. %-10s fn=%s version=%s" % (path, fn["sid"], ver["sid"]))

    # 3. environment
    envs = req("GET", f"{base}/{ssid}/Environments?PageSize=20").get("environments", [])
    env = next((e for e in envs if e["unique_name"] == "prod"), None)
    if env:
        print("3. environment exists:", env["sid"], env["domain_name"])
    else:
        env = req("POST", f"{base}/{ssid}/Environments", {"UniqueName": "prod", "DomainSuffix": "prod"})
        print("3. environment created:", env["sid"], env["domain_name"])
    esid, domain = env["sid"], env["domain_name"]

    # 4. variables
    cur = {v["key"]: v for v in req("GET", f"{base}/{ssid}/Environments/{esid}/Variables?PageSize=50").get("variables", [])}
    for k, v in (("FORWARD_TO", FORWARD_TO), ("TWILIO_NUMBER", NUMBER)):
        if k in cur:
            req("POST", f"{base}/{ssid}/Environments/{esid}/Variables/{cur[k]['sid']}", {"Value": v})
            print("4. variable updated %s=%s" % (k, v))
        else:
            req("POST", f"{base}/{ssid}/Environments/{esid}/Variables", {"Key": k, "Value": v})
            print("4. variable set     %s=%s" % (k, v))

    # 5. build
    payload = [("FunctionVersions", v) for v in versions]
    payload.append(("Dependencies", json.dumps(DEPENDENCIES)))
    payload.append(("Runtime", "node24"))
    build = req("POST", f"{base}/{ssid}/Builds", payload)
    bsid = build["sid"]
    print("5. build:", bsid, build["status"])
    for _ in range(60):
        time.sleep(5)
        st = req("GET", f"{base}/{ssid}/Builds/{bsid}")["status"]
        if st in ("completed", "failed"):
            print("   build", st)
            if st == "failed":
                raise SystemExit("build failed")
            break
        print("   ...", st)

    # 6. deploy
    dep = req("POST", f"{base}/{ssid}/Environments/{esid}/Deployments", {"BuildSid": bsid})
    print("6. deployed:", dep["sid"])

    # 7. point the phone number at /incoming
    voice_url = f"https://{domain}/incoming"
    nums = req("GET", f"https://api.twilio.com/2010-04-01/Accounts/{SID}/IncomingPhoneNumbers.json?PhoneNumber={urllib.parse.quote(NUMBER)}")
    num = nums["incoming_phone_numbers"][0]
    upd = req("POST", f"https://api.twilio.com/2010-04-01/Accounts/{SID}/IncomingPhoneNumbers/{num['sid']}.json", {
        "FriendlyName": "Kissimmee Concrete Main Line (689) 263-6255",
        "VoiceUrl": voice_url,
        "VoiceMethod": "POST",
        "StatusCallbackMethod": "POST",
    })
    print("7. number %s -> %s" % (upd["phone_number"], upd["voice_url"]))
    print("\nDONE  domain=%s  forward=%s" % (domain, FORWARD_TO))
    return voice_url


if __name__ == "__main__":
    main()
