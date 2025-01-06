from flask import Flask, request, jsonify
import joblib
import traceback

# Initialize Flask app
app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('../models/logistic_regression_model.pkl')
vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')

# Home route
@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API!"

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        transformed_text = vectorizer.transform([text])
        prediction = model.predict(transformed_text)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"
        return jsonify({"text": text, "sentiment": sentiment})

    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
