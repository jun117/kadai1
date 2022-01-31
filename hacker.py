import requests

topstories = "8863"
url = f"https://hacker-news.firebaseio.com/v0/item/{topstories}.json"

response = requests.get(url)

dic = response.json()
news_title = dic["title"]
news_link = dic["url"]
print(f"'title':'{news_title}','link':'{news_link}'")

"""
print((response))
print(response.json()['id'])
print(type(response.json()))
"""
