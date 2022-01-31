import requests


def search_url_list():
    url_list = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response_list = requests.get(url_list)
    dic_lists = response_list.json()
    return dic_lists


def search_news(dic_list):
    url = f"https://hacker-news.firebaseio.com/v0/item/{dic_list}.json"
    response = requests.get(url)
    dic = response.json()
    news_title = dic["title"]
    news_link = dic["url"]
    results = f"'title':'{news_title}','link':'{news_link}'"
    return results


def main():
    dic_lists = search_url_list()

    for dic_list in dic_lists:
        results = search_news(dic_list)

        print(results)


if __name__ == '__main__':
    main()
