// Download the twilio-csharp library from twilio.com/docs/csharp/install
using System;
using Twilio;
class Example 
{
  static void Main(string[] args) 
  {
    // Find your Account Sid and Auth Token at twilio.com/user/account
    string AccountSid = "AC1365ff479ef6502d85c27be6467a310c";
    string AccountSidToSuspend = "ACxxxxxxxxxxxxxxxxxxx";
    string AuthToken = "{{ auth_token }}";
    var twilio = new TwilioRestClient(AccountSid, AuthToken);
    Account account = twilio.ChangeSubAccountStatus(AccountSidToSuspend, Twilio.AccountStatus.Suspended);
  }
}