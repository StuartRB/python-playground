from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "cheese"


@app.route("/peas", methods=['POST', 'GET'])
def peas():
    return "peas"


@app.route("/sandwich/<filling>")
def sandwich(filling):
    return f'I also enjoy {filling} sandwiches'

@app.route('/post', methods=['POST'])
def post_data():
    # Access the data sent with the POST request
    data = request.json

    # Process the data...
    # For example, let's assume the data is a JSON object with a key 'message'
    if 'message' in data:
        response_message = f"Received message: {data['message']}"
    else:
        response_message = "No message received"

    # Return a response
    return jsonify({'response': response_message})

app.run(host="0.0.0.0", port=5001)
