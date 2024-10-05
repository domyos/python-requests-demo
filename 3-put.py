import requests

# URL and data to be updated
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "foo updated",
    "body": "bar updated",
    "userId": 1
}

# Send PUT request
response = requests.put(url, json=data)

# Check status code and print the response
print(response.status_code)
print(response.json())

