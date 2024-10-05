import requests

# Send a GET request
url = "https://httpbin.org/cookies/set/sessioncookie/123456"
response = requests.get(url)

# Get cookies from the response
cookies = response.cookies

# Iterate through cookies
for cookie in cookies:
    print(f"Cookie: {cookie.name} = {cookie.value}")

# Access specific cookie
print(cookies.get('sessioncookie'))

