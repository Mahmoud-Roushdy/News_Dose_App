from colorama import Fore, Style, init
from userRepository import UserReposiotry
from article_manger import ArticleManger
from ai_assistant import Ai_assistant
from feed_manger import Feed_Manager
from formatter import Formatter
from news_api_Manger import NewsApiManger
from feed_repository import Feed_Repository
from feed import Feed
from agency_repository import AgencyRepository
from agency import Agency


init()  # to reset color while printing in terminal...

"""
 Main function docomentation =>
the main function which is represent the entry for News Dose App. it has all posible options related to the App.
 - option 1 -> fetch the news in feed table which has the Rss links for well-known and wide-spreaded newspapers.
 - option 2 -> you can search newspapers around the internet about keyword, for examaple: Apple, Tesla,Trump,Germany,AI.
 - option 3 -> possibly can get news about certain category. For example; health, technolgy,education, etc.
 - option 4 -> easily get the full article even newspapers articles needed to be a subscriper! 
               this option haas been built with AI assistant as you can get article summary, and article anlysis.
 - option 5 -> represent all current feeds you can fetch in the option 1.
 - option 6 -> represent feed setting as you can easily add or delete a feed.
 -  option 7 -> represent all newspapers rss. you can know all posible rss agencies, delete or add a new agency.
 - option 8 -> represent user setting as you have the ability to edit or delete your user name. 
"""


def main():
    print(Fore.RED + Style.BRIGHT + "📢 Welcome in News Dose 📢")
    check_user()
    while True:
        get_options()
        user_input = input(Fore.BLACK + Style.BRIGHT + "📝insert an option: ")
        if user_input == "1":
            print_option_one()
        elif user_input == "2":
            print_option_two()
        elif user_input == "3":
            print_option_three()
        elif user_input == "4":
            print_option_four()
        elif user_input == "5":
            prtint_option_five()
        elif user_input == "7":
            print_option_seven()
        elif user_input == "8":
            print_option_eight()

        elif user_input == "9":
            user_options()

        elif user_input == "" or "0":
            break

        print("\n" + "▀" * 60)


def get_options():
    print(Fore.YELLOW + Style.BRIGHT + "📡 News Dose Options 📡")
    print(Fore.CYAN + Style.NORMAL + " 1-Get News ()")
    print(Fore.CYAN + Style.NORMAL + " 2-Search By Keyword")
    print(Fore.CYAN + Style.NORMAL + " 3-Get News By Category")
    print(Fore.CYAN + Style.NORMAL + " 4-Get Full Article)")
    print(Fore.CYAN + Style.NORMAL + " 5-Show My Current Feeds")
    print(Fore.CYAN + Style.NORMAL + " 6-Chat with News")
    print(Fore.CYAN + Style.NORMAL + " 7-Feeds Setting")
    print(Fore.CYAN + Style.NORMAL + " 8-Agencies Setting")
    print(Fore.CYAN + Style.NORMAL + " 9-User Setting")

    print(Fore.CYAN + " ⎋ Press Enter to Exit ")


# to check if App has a user or not, and return a user name
def check_user():
    userrepo = UserReposiotry()
    if userrepo.check_user() == True:
        user = userrepo.get_user()
        print(f"{Fore.BLUE + Style.BRIGHT} Welcome back {user}")
    else:
        user_input = input(f"{Fore.YELLOW + Style.DIM} Enter your user name: ")
        userrepo.create_user(user_input)
        print(f"{Fore.BLUE + Style.BRIGHT} Welcome in your news Dose App,{user_input}")


# print news list in option one
def print_option_one():
    feedlist = Feed_Manager().parse_news()

    for list in feedlist:
        feedname = list["feed_name"]

        formatter = Formatter()
        print(formatter.format_feed_name(feedname))

        for news in list["news_list"]:

            print(formatter.format_news(news))


# print option  data
def print_option_two():
    user_input = input(f"{Fore.YELLOW + Style.BRIGHT} Write a Keyword to search: ")
    print(f"{Fore.BLUE} Fetching news.....")
    NewsApi = NewsApiManger()
    formatter = Formatter()
    result = NewsApi.Search_by_keyword(user_input)
    for row in result:
        print(formatter.format_news(row))


def print_option_three():
    print(
        f"{Fore.RED + Style.BRIGHT}Possible Catogories:{Fore.CYAN + Style.DIM}Healh - Sports- technology- Entertainment- Science- Business"
    )
    print_option_two()


def print_option_four():
    url = input(f"{Fore.BLUE +Style.DIM} Paste Article Url here: ")
    articlemanger = ArticleManger(url).fetch_url()
    print(
        f"{Fore.RED + Style.BRIGHT} Article Title: {Fore.YELLOW}{articlemanger.title}"
    )
    print(
        f"{Fore.RED + Style.BRIGHT} Article Content:\n {Fore.WHITE}{articlemanger.fulltext}\n"
    )

    get_ai_options(articlemanger.fulltext)


def get_ai_options(article):
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Ai Assisstant")
    print(Fore.CYAN + Style.NORMAL + " 1- Get Article Summary")
    print(Fore.CYAN + Style.NORMAL + " 2-Article Analyzing")
    print(Fore.CYAN + Style.NORMAL + " 0- Get back to main options")
    user_input = input(Fore.MAGENTA + Style.DIM + "Enter your option number: ")
    ai_assisstant = Ai_assistant(article)
    if user_input == "1":
        result = ai_assisstant.summarize_article()
        print(Fore.BLUE + Style.BRIGHT + result)
        get_ai_options(article)

    if user_input == "2":
        result = ai_assisstant.analize_article()

        print(Fore.CYAN + Style.DIM + result)
        get_ai_options(article)

    if user_input == "0":
        main()


def prtint_option_five():
    feedrepo = Feed_Repository()
    all_feeds = feedrepo.get_all_feeds()
    for feeddict in all_feeds:
        print(
            f"{Fore.RED + Style.BRIGHT} Feed Name: {Fore.YELLOW}{feeddict['feed_name']} {Fore.BLUE + Style.DIM}URL: {feeddict['url']}"
        )


def print_option_seven():

    print(Fore.CYAN + Style.NORMAL + " 1-Add Feed:")
    print(Fore.CYAN + Style.NORMAL + " 2-Delete Feed")
    user_input = input(Fore.MAGENTA + Style.DIM + "Enter your option number: ")
    feedrepo = Feed_Repository()
    if user_input == "1":

        user_insert_agency_name = input(f"{Fore.BLUE +Style.DIM} Write feed name: ")
        user_insert_agency_url = input(f"{Fore.BLUE +Style.DIM} Write feed url: ")
        feed = Feed(user_insert_agency_name, user_insert_agency_url)
        print(feedrepo.add_feed(feed))
    if user_input == "2":
        feed_to_delete = input(f"{Fore.BLUE +Style.DIM} Write feed name to delete: ")
        print(feedrepo.delete_feed(feed_to_delete))
    main()


def print_option_eight():
    print(Fore.CYAN + Style.NORMAL + " 1-Show All Agencies:")
    print(Fore.CYAN + Style.NORMAL + " 2-Add Agency:")
    print(Fore.CYAN + Style.NORMAL + " 3-Delete Agency")
    user_input = input(Fore.MAGENTA + Style.DIM + "Enter your option number: ")
    agencyrepo = AgencyRepository()

    if user_input == "1":
        all_agencies = agencyrepo.get_all()
        print(Fore.RED + Style.BRIGHT + "All Agencies:")
        for agency in all_agencies:
            print(
                f"{Fore.RED + Style.BRIGHT} Agency Name: {Fore.YELLOW}{agency['name']} {Fore.BLUE + Style.DIM}URL: {agency['link']}"
            )
    elif user_input == "2":
        user_insert_agency_name = input(f"{Fore.BLUE +Style.DIM} Write Agency name: ")
        user_insert_agency_url = input(f"{Fore.BLUE +Style.DIM} Write Agency url: ")
        agency = Agency(user_insert_agency_name, user_insert_agency_url)
        print(agencyrepo.add_agency(agency))
    elif user_input == "3":
        feed_to_delete = input(f"{Fore.BLUE +Style.DIM} Write feed name to delete: ")
        print(agencyrepo.delete_Agency(feed_to_delete))


def option_6():
    print(Fore.CYAN + Style.NORMAL + " 1-Summarize your article:")
    print(Fore.CYAN + Style.NORMAL + " 2-Get comberhnsive Anlysis")
    user_input = input(Fore.MAGENTA + Style.DIM + "Enter yoyr option number: ")
    if user_input == "1":
        Ai_assistant.summarize_article()
    main()


def user_options():
    print(Fore.CYAN + Style.NORMAL + " 1-Edit user:")
    print(Fore.CYAN + Style.NORMAL + " 2-Delete")
    user_input = input(Fore.MAGENTA + Style.DIM + "Enter your option number: ")
    userrepo = UserReposiotry()
    if user_input == "1":
        new_user = input(Fore.MAGENTA + Style.DIM + "Enter new name: ")
        userrepo.edit_user(new_user)
    if user_input == "2":
        userrepo.delete_user()
    main()


def feed_setting():
    print(Fore.RED + "Reminder: you can only add 3 Agencies")
    print(Fore.CYAN + Style.NORMAL + " 1-Add Agency:")
    print(Fore.CYAN + Style.NORMAL + " 2-Delete Agency")
    user_input = input(Fore.MAGENTA + Style.DIM + "Enter your option number: ")
    if user_input == "1":
        # RSS_Feed.add_feed()
        pass
    if user_input == "2":
        # RSS_Feed.delete_feed()
        pass
    main()


if __name__ == "__main__":

    main()
4
