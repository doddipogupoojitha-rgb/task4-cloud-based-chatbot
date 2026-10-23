from flask import Flask, render_template, request, jsonify
import json, random, os

app = Flask(__name__)

with open('intents.json') as f:
    intents = json.load(f)

def get_response(msg):
    msg=msg.lower()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in msg:
                return random.choice(intent['responses'])
    if "hi" in msg or "hello" in msg:
        return "Hello! I'm your cloud assistant 😊 How can I help?"
    elif "bye" in msg:
        return "Goodbye! Have a great day! 👋"
    else:
        return "I can help with support, services, and general queries. Please rephrase!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def bot_response():
    user_msg = request.json.get('message','')
    return jsonify({"response": get_response(user_msg)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
