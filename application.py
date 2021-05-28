from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, This is Kims Azure Web App using Flask!"

@app.route("/smsold", methods=['GET', 'POST'])
def sms_reply():
    # Respond to incoming calls with a simple text message.
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("This is a reply from the Azure Web App using Twilio & Flask")

    return str(resp)
    
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    # Send a dynamic reply to an incoming text message
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == '1':
        resp.message("Great! See you for that shift")
    elif body == '2':
        resp.message("Go find coverage for that shift")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
