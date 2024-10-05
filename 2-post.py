import requests

# URL and data to be posted
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Send POST request
response = requests.post(url, json=data)

# Check status code and print the response
print(response.status_code)
print(response.json())  # Assuming the response is JSON

