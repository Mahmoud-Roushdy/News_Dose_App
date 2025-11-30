from tinydb import TinyDB, Query
from colorama import Fore, Style
from user import User


class UserReposiotry:

    def __init__(self, db_path="news_db.json"):
        self.db = TinyDB(db_path)
        self.table = self.db.table("User")
        # user.total += 1

    def create_user(self, user_name):
        user = User(user_name)
        try:

            self.table.insert({"user_name": user.name})
            return "User added successfully!!"

        except ConnectionError as e:
            return f"Error took place!{e}"

    def get_user(self):
        query = Query()
        for user in self.table:
            return user["user_name"]

    def check_user(self):
        return len(self.table) > 0

    def delete_user(self):
        if len(self.table) == 0:
            return f"No User found!"
        else:
            try:
                current_user = self.get_user()
                query = Query()
                self.table.remove(query.user_name == current_user)
                return "Successfully removed!"
            except ValueError as e:
                return f"Error took place: {e}"

    def edit_user(self, name):
        if len(self.table) == 0:
            return "No User found!"
        else:
            query = Query()
            self.table.update({"user_name": name}, query.user_name == self.get_user())
            return "Successfully Edited!!"


if __name__ == "__main__":

    userrepo = UserReposiotry()
    edit_user = userrepo.check_user()
    print(edit_user)
