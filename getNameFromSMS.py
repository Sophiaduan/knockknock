from flask import Flask, request
from twilio import twiml
# ngrok http 5000
# python getNameFromSMS.py

 
app = Flask(__name__)
 
@app.route('/sms', methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	f = open('smsMessage.txt', 'w')
	f.write(number + "\n")
	f.write(message_body)
	f.close()

	resp = twiml.Response()
	content = message_body.split(",")

	if (len(content) > 0 and (content[0] == "YES" or content[0] == "Yes" or content[0] == "yes")):
		resp.message('\nThe door is opening!')
	elif (len(content) > 0 and (content[0] == "NO" or content[0] == "No" or content[0] == "no")):
		resp.message('\nWe have secured the door!')
	return str(resp)
 
if __name__ == '__main__':
    app.run()