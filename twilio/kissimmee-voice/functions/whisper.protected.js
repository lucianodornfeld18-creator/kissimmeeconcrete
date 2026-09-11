exports.handler = function (context, event, callback) {
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
