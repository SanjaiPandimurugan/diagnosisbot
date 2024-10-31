import requests
import json

# Define the URL of the Flask application
url = 'http://127.0.0.1:5000/diagnose'

# Define test cases
test_cases = [
    {"age": 30, "vital_signs": "120,80", "ecg": 0.5, "pulse": 72, "temperature": 98.6},
    {"age": 45, "vital_signs": "150,95", "ecg": 0.8, "pulse": 80, "temperature": 100.0},
    {"age": 60, "vital_signs": "180,110", "ecg": 1.1, "pulse": 88, "temperature": 101.5},
    {"age": 25, "vital_signs": "110,70", "ecg": 0.4, "pulse": 70, "temperature": 98.0},
    {"age": 50, "vital_signs": "160,100", "ecg": 0.9, "pulse": 85, "temperature": 100.5}
]

# Loop through each test case and send a request
for i, test_case in enumerate(test_cases):
    # Prepare the JSON payload
    payload = json.dumps(test_case)
    
    # Send a POST request to the Flask application
    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=payload)
    
    # Print the response
    print(f"Test Case {i + 1}: {test_case}")
    print(f"Response: {response.json()}\n")