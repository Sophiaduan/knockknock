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

    resp = twiml.Response()
    resp.message('\nThank you for your response.  Next time, I will recognize this person as {}.'.format(message_body))
    return str(resp)
 
if __name__ == '__main__':
    app.run()