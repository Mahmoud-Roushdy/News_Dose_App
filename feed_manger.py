from feed_repository import Feed_Repository
from feed_source import Feed_Souce
from feed import Feed
from feedparser import parse
from news import News


class Feed_Manager:

    def __init__(self, feedrepo=Feed_Repository()):
        self.__feedrepository = feedrepo

    def parse_news(self):
        headlines = []
        feedlist = self.__feedrepository.get_all_feeds()

        for feed in feedlist:
            url = ""
            url = feed["url"]
            feedsource = Feed_Souce(url)
            response = feedsource.fetch_feed()
            feed_parsed = parse(response)
            if "title" not in feed_parsed["feed"]:
                continue

            feed_name = feed_parsed["feed"]["title"]
            list_news = []
            for entry in feed_parsed["entries"][:10]:

                news = News(entry["title"], entry["summary"], entry["link"])

                list_news.append(news)
            headlines.append({"feed_name": feed_name, "news_list": list_news})

        return headlines


if __name__ == "__main__":
    feedmanger = Feed_Manager()
    feedlist = feedmanger.parse_news()
    print(feedlist)
