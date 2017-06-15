from twilio.rest import TwilioRestClient

account = "AC1988cd4a82dbb4df28d30cfe791d5c6e"
token = "bdfc84e0fdad11bf455c9d1846842574"
client = TwilioRestClient(account, token)

def sendText(URL, body_message, phoneSTR): #e.g. sendText("google.com", "His name is Matt", PHONENO)
	message = client.messages.create(
	    body = body_message,  # Message body, if any
	    to = phoneSTR,
	    from_= "+17657692087",
	    media_url= [  # List of media URLs, if any
	        URL,
	    ],
	)
def sendSMS(body_message, phoneSTR):
		message = client.messages.create(
	    body = body_message,  # Message body, if any
	    to = phoneSTR,
	    from_= "+17657692087",
	)

#sendText("http://i.imgur.com/cX7kkGN.png", "This is Ajay and Natat", PHONENO)
