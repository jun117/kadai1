import requests
import time


def main():
    response_list = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    dic_lists = response_list.json()

    for dic_list in dic_lists:
        url_text = f"https://hacker-news.firebaseio.com/v0/item/{dic_list}.json"
        response = requests.get(url_text)
        if 'url' in response.json():
            news_title = response.json()['title']
            news_link = response.json()['url']
            for i in range(3):
                time.sleep(1)

            print(f"'title':'{news_title}','link':'{news_link})'")


if __name__ == '__main__':
    main()
