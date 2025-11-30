from agency import Agency
from tinydb import TinyDB, Query


class AgencyRepository:
    def __init__(self, db_path="news_db.json"):
        self.db = TinyDB(db_path)
        self.table = self.db.table("agencies")

    def get_all(self):
        return self.table.all()

    def get_by_name(self, name):
        query = Query()
        return self.table.get(query.name == name)

    def add_agency(self, agency):
        if agency is None:
            return "invalid agency name or agency link"
        else:
            self.table.insert({"name": agency.name, "link": agency.link})
            return "Successfully added!"

    def delete_Agency(self, agency):
        if agency is None:
            return "invalid agency name!"
        else:
            query = Query()
            self.table.remove(query.name == agency)
            return "deleted successfully!"


if __name__ == "__main__":
    agencyrepo = AgencyRepository()
    agency = "google"
    print(agencyrepo.get_by_name("BBC News"))
