from twilio.rest import TwilioRestClient

account = "AC1988cd4a82dbb4df28d30cfe791d5c6e"
token = "bdfc84e0fdad11bf455c9d1846842574"
client = TwilioRestClient(account, token)

message = client.sms.messages.create(to="+17654045543",
                                     from_="+17657692087",
                                     body="Hello there!  Working on face detection")