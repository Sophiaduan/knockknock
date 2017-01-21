import pyimgur
from twilio.rest import TwilioRestClient

account = "AC1988cd4a82dbb4df28d30cfe791d5c6e"
token = "bdfc84e0fdad11bf455c9d1846842574"
client = TwilioRestClient(account, token)
CLIENT_ID = "100ef2fd6ae00e0"

def sendText(PATH):
	im = pyimgur.Imgur(CLIENT_ID)
	uploaded_image = im.upload_image(PATH, title="Face recognize your friends")
	print(uploaded_image.title)
	print(uploaded_image.link)
	print(uploaded_image.size)
	print(uploaded_image.type)

	message = client.messages.create(
	    body="My picture!",  # Message body, if any
	    to="+17654045543",
	    from_="+17657692087",
	    media_url=[  # List of media URLs, if any
	        uploaded_image.link,
	    ],
	)
sendText("Face1.png")