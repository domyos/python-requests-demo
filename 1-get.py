import requests

# URL you want to send a request to
url = "https://makerspace-esslingen.de"

# Send GET request
response = requests.get(url)

# Check status code (200 means OK)
print(response.status_code)

# Print the response content
print(response.text)

