var accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
var authToken = '{{ auth_token }}';
var Twilio = require('twilio');

var client = new Twilio(accountSid, authToken);

client.notifications.v1.services.create({
  friendlyName: 'My Awesome Service'
}).then(function(response) {
  console.log(response);
}).catch(function(error) {
  console.log(error);
});