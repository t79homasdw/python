import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("Success!")
    print(response.json())
    print(response.json()["userId"])
else:
    print("Failed to fetch data. Status code:", response.status_code)

    