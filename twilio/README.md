# Twilio voice — Kissimmee Concrete

Live number **(689) 263-6255** → forwards to **(689) 242-7487**, mirroring the
`ocoee-voice` and `windermere-voice` services on the same account.

| | |
|---|---|
| Service | `kissimmee-voice` (`ZS55905c11fb4105430507f18bd7216194`) |
| Environment | `prod` → `kissimmee-voice-9865-prod.twil.io` |
| Variables | `FORWARD_TO=+16892427487`, `TWILIO_NUMBER=+16892636255` |
| Number webhook | `POST https://kissimmee-voice-9865-prod.twil.io/incoming` |
| Runtime | node24, `twilio@5.0.3` |

## Call flow

1. **`/incoming`** — the caller hears *"Thanks for calling Kissimmee Concrete.
   Press any key to be connected."* twice, slowed to 85%. No keypress hangs up,
   which filters out autodialers before the owner's phone ever rings.
2. After a keypress the caller hears *"One moment while we connect you"* and
   Twilio dials `FORWARD_TO` with the caller's own number as caller ID, a
   20-second timeout and dual-channel recording from answer.
3. **`/whisper`** — plays only on the owner's leg: a 2-second pause for mobile
   audio to open, then *"New lead from Kissimmee Concrete. Press any key to
   accept."* twice. No keypress hangs up that leg only.
4. **`/accept`** — empty TwiML, which ends the screening and bridges the call.
5. **`/voicemail`** — reached when the call was not accepted, was busy or
   failed. Records up to 120 seconds with transcription, then thanks and hangs
   up. A bridged call that simply ended lands here too and is hung up silently.

## Redeploy

```bash
TWILIO_SID=... TWILIO_TOKEN=... python twilio/deploy_kissimmee_voice.py
```

The script is idempotent: it reuses the service, functions and environment if
they exist, uploads new function versions, rebuilds, redeploys and re-points the
number. Credentials are read from the environment and never stored in the repo.

## Verify without calling

Protected functions require a valid `X-Twilio-Signature`, so a plain GET returns
403. To exercise the flow, sign the request with the auth token
(HMAC-SHA1 of the full URL plus the sorted POST parameters, base64) and POST to
`/incoming`, `/whisper`, `/accept` and `/voicemail` in turn.
