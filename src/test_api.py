import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"

# Define the test input
data = {
    "text": "This movie was absolutely amazing!"
}

# Send a POST request to the API
response = requests.post(url, json=data)

# Print the response
print("Response:", response.json())


