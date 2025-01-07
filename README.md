# Sentiment Analysis System

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Installation and Usage](#installation-and-usage)
- [API Usage](#api-usage)
- [Results](#results)
- [Dataset](#dataset)
- [Testing the API](#testing-the-api)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview
This project implements a **Sentiment Analysis System** to classify text reviews as **positive** or **negative**. It uses the **IMDB Movie Reviews Dataset** for training and evaluates a machine learning model based on **TF-IDF vectorization** and **Logistic Regression**. The system is deployed as a **Flask API** for real-time sentiment predictions.

---

## Key Features
- **Data Preprocessing:** Cleaned and tokenized text data using Python libraries like `re`, `nltk`, and `pandas`.
- **Feature Engineering:** Used **TF-IDF vectorization** to convert text into numerical features.
- **Model Training:** Trained a **Logistic Regression model** for binary classification.
- **Deployment:** Hosted a Flask API for real-time predictions.
- **Testing:** Provided a test script to validate the API.
- **Performance Visualization:** Results visualized using metrics like accuracy and F1-score.

---

## Project Structure
Sentiment-Analysis-System/
├── data/                        # Dataset folder
│   ├── IMDB Dataset.csv         # Raw dataset
│   ├── processed_data.csv       # Preprocessed dataset
├── models/                      # Folder for saved models
│   ├── logistic_regression_model.pkl
│   ├── tfidf_vectorizer.pkl
├── src/                         # Source code for the Flask API
│   ├── app.py                   # Flask API implementation
│   ├── test_api.py              # Script to test the API
├── notebook/                    # Jupyter Notebook for end-to-end workflow
│   ├── sentiment_analysis.ipynb
├── requirements.txt             # List of Python dependencies
├── Dockerfile                   # Docker configuration for deployment
├── LICENSE                      # License information
└── README.md                    # Documentation






---

---

## Installation and Usage

### Prerequisites
- **Python 3.8** (Ensure compatibility)
- Virtual environment (optional but recommended)

### Steps to Run

### 1. Clone the Repository

git clone https://github.com/himanshu-dandle/Sentiment-Analysis-System.git
cd Sentiment-Analysis-System

### 2. Install Dependencies

python -m venv venv
venv\Scripts\activate          # Activate on Windows
pip install -r requirements.txt


### 3. . Run the Flask API
Navigate to the src/ folder and start the Flask app:
cd src
python app.py

The API will be available at http://127.0.0.1:5000.



API Usage
Endpoints
1. Home Endpoint:

	URL: http://127.0.0.1:5000/
	Method: GET
	Description: Returns a welcome message.

2.Prediction Endpoint:

	URL: http://127.0.0.1:5000/predict
	Method: POST
	Description: Predicts the sentiment of the input text.
	Request Body (JSON):
			json

			{
				"text": "This movie was fantastic!"
			}
	Response (JSON):
	json

	{
		"text": "This movie was fantastic!",
		"sentiment": "Positive"
	}
Results
	Accuracy: 88% on the test dataset.
	Classification Report:

			precision   recall  f1-score   support

	  Negative        0.89      0.86      0.88      4961
	  Positive        0.87      0.90      0.88      5039

	  accuracy                           0.88      10000
	  macro avg       0.88      0.88      0.88     10000
	  weighted avg    0.88      0.88      0.88     10000

Dataset
The dataset used is the IMDB Movie Reviews Dataset. Download it and place the file (IMDB Dataset.csv) in the data/ folder.

Testing the API
Use the test_api.py script to send a POST request and validate the /predict endpoint:

	python src/test_api.py
	
Future Enhancements
	Replace Logistic Regression with a BERT-based model for improved performance.
	Add sentiment trend analysis over time.
	Deploy the API using Docker or a cloud service like AWS or Azure.
License
	This project is open-source and available under the MIT License.

Acknowledgments
	scikit-learn
	Flask
	IMDB Dataset


