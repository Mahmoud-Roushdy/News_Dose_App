from colorama import Fore, Style, init
from news import News

init()


class Formatter:
    def __init__(self, color=Fore, style=Style):

        self.color = color
        self.style = style

    def format_news(self, news):
        return (
            f"{self.color.RED + Style.BRIGHT}Title: {self.color.WHITE + self.style.BRIGHT} {news.title}\n"
            f"{self.color.RED + Style.BRIGHT}Summary: {self.color.YELLOW +self.style.DIM} {news.summary}\n"
            f"{self.color.RED + Style.BRIGHT}Website: {self.color.BLUE + self.style.DIM} {news.link}\n"
        )

    def format_feed_name(self, name):
        return f"{self.color.RED + self.style.BRIGHT}Feed Name: {name}\n"


if __name__ == "__main__":
    formatter = Formatter()
    news = News("Ahmed", "Ali", "google.com")
    print(formatter.format_feed_name("mahmoud"))
    print(formatter.format_news(news))
