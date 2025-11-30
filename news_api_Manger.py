from datetime import datetime, timedelta
from feed_source import Feed_Souce
from news import News


class NewsApiManger:

    ApiKey = "9949e3983a8440cf81416641c948e9f3"

    def __init__(self, Api_key=ApiKey):
        self.ApiKey = Api_key

    def Search_by_keyword(self, word):
        catogeries = [
            "technology",
            "business",
            "sports",
            "education",
            "general",
            "entertainment",
            "health",
        ]
        if word in catogeries:
            link = f"https://newsapi.org/v2/top-headlines?category={word}&apiKey={self.ApiKey}"
        else:
            link = f"https://newsapi.org/v2/top-headlines?q={word}&apiKey={self.ApiKey}"

        feedsource = Feed_Souce(link).fetch_feed()
        articles = feedsource["articles"][:20]
        return self.format(articles)

    def format(self, newslist):
        headlines = []
        for newsdict in newslist:
            news = News(newsdict["title"], newsdict["description"], newsdict["url"])
            headlines.append(news)
        return headlines


if __name__ == "__main__":
    newsapi = NewsApiManger()
    result = newsapi.Search_by_keyword("trump")
    print(len(result))
