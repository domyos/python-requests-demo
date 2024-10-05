import requests

# URL you want to send a request to
url = "https://example.com"

# Define cookies in a dictionary
cookies = {'session_id': '123456', 'user_token': 'abcdef'}

# Send GET request with cookies
response = requests.get(url, cookies=cookies)

# Check response
print(response.status_code)
print(response.text)  # Print the response content

