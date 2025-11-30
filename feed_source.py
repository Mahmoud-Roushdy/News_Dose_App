from requests import get


class Feed_Souce:

    def __init__(self, link):
        self.link = link

    def fetch_feed(self):
        if self.link is None:
            print("link is not vaild")
        try:

            response = get(self.link)
            if response.status_code == 200:
                if "newsapi" in self.link:
                    return response.json()
                elif "xml" or "rss" in self.link:
                    return response.text
                else:
                    return "unsupported-content-type response"
            else:
                return "failed response"
        except Exception as e:
            return f"Error took place: {e}"


if __name__ == "__main__":

    feedsource = Feed_Souce("http://feeds.bbci.co.uk/news/rss.xml")
    print(feedsource.fetch_feed())
