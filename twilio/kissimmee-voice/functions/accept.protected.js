exports.handler = function (context, event, callback) {
  // Empty TwiML ends call screening and bridges the two legs.
  const twiml = new Twilio.twiml.VoiceResponse();
  return callback(null, twiml);
};
