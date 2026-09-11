exports.handler = function (context, event, callback) {
  const twiml = new Twilio.twiml.VoiceResponse();

  if (event.Digits) {
    // Caller pressed a key -> proceed with the normal dial flow.
    twiml.say(
      { voice: 'Polly.Matthew-Neural' },
      'One moment while we connect you.'
    );
    const callerId = /^\+\d+$/.test(event.From) ? event.From : context.TWILIO_NUMBER;
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
