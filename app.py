from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['input']])
    return jsonify({'prediction': int(prediction[0])})

@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
