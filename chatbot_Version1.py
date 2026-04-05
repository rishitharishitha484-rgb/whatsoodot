from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()

    response = MessagingResponse()
    msg = response.message()

    if "hello" in incoming_msg:
        msg.body("Hi 👋 Welcome! How can I help you?")
    elif "help" in incoming_msg:
        msg.body("Available commands:\n1. hello\n2. info\n3. bye")
    elif "info" in incoming_msg:
        msg.body("This is a chatbot built using Flask + Twilio 🤖")
    elif "bye" in incoming_msg:
        msg.body("Goodbye! Have a nice day 😊")
    else:
        msg.body("Sorry, I didn't understand that.")

    return str(response)

if __name__ == "__main__":
    app.run()