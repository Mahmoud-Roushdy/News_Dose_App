from tinydb import TinyDB, Query
from feed import Feed
from agency_repository import AgencyRepository


class Feed_Repository:
    def __init__(self, db_path="news_db.json"):
        self.__db = TinyDB(db_path)
        self.__table = self.__db.table("feeds")

    def get_all_feeds(self):
        all_feeds = self.__table.all()
        return all_feeds

    def add_feed(self, feed):
        self.__table.insert({"feed_name": feed.name, "url": feed.url})
        return "Feed added successuflly!"

    def delete_feed(self, feed):
        query = Query()
        self.__table.remove(query.feed_name == feed)
        return "feed reomved succcessuflly!!"

    def is_exist(self, feedname):
        all_feeds = self.get_all_feeds()
        for feed_dict in all_feeds:
            if feed_dict["feed_name"] == feedname:
                return True
        else:
            return False

    def choose_agency(self, agencyname):
        agencyrepo = AgencyRepository()
        agency_to_add = agencyrepo.get_by_name(agencyname)
        agency_to_feed = Feed(agency_to_add["name"], agency_to_add["link"])
        self.add_feed(agency_to_feed)
        return "Agency added successfuly to your feeds!"


if __name__ == "__main__":
    # feed = Feed("BBC News", "http://feeds.bbci.co.uk/news/rss.xml")
    feedrepo = Feed_Repository()
    # feedrepo.add_feed(feed=Feed("BBC News", "http://feeds.bbci.co.uk/news/rss.xml"))
    agency = "CNN (World)"
    print(feedrepo.choose_agency(agency))
