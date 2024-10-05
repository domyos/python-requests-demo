import requests

# URL of the resource to be deleted
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send DELETE request
response = requests.delete(url)

# Check status code
print(response.status_code)

