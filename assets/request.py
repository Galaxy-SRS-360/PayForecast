# Import the 'requests' library to send HTTP requests
import requests  # For making HTTP requests

# Define the URL for the API endpoint
url = 'http://localhost:8000/predict_api'

# Create a POST request with JSON data (years of experience, test score, interview score)
# and send it to the specified API endpoint
r = requests.post(url, json={'experience': 6, 'test_score': 6, 'interview_score': 6})

# Print the JSON response received from the API endpoint
print(r.json())
