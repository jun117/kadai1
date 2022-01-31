import requests
import time


def search_dic():
    url_list = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response_list = requests.get(url_list)
    dic_lists = response_list.json()
    return dic_lists


def search_list():
    dic_lists = search_dic()
    for dic_list in dic_lists:
        url_text = f"https://hacker-news.firebaseio.com/v0/item/{dic_list}.json"

        response = requests.get(url_text)

        dic = response.json()

        if 'url' in dic:
            news_title = dic['title']
            news_link = dic['url']
            for i in range(10):
                time.sleep(1)

            print(f"'title':'{news_title}','link':'{news_link})'")


def main():
    search_list()


if __name__ == '__main__':
    main()
