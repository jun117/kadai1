import requests

url_list = "https://hacker-news.firebaseio.com/v0/topstories.json"
response_list = requests.get(url_list)

dic_lists = response_list.json()

for dic_list in dic_lists:
    url = f"https://hacker-news.firebaseio.com/v0/item/{dic_list}.json"

    response = requests.get(url)

    dic = response.json()
    news_title = dic["title"]
    news_link = dic["url"]

    print(f"'title':'{news_title}','link':'{news_link}'")
