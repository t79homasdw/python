import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in the POST request
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Post request successful!")
    print("Response:", response.json())
else:
    print("Failed to make a post request. Status code:", response.status_code)