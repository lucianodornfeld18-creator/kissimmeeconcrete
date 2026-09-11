exports.handler = function (context, event, callback) {
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
