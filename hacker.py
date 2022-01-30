import requests

url = "https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty"

response = requests.get(url)

print(response)
print(response.text)
