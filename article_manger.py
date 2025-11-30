from article import Article
from requests import get
from bs4 import BeautifulSoup
from ai_assistant import Ai_assistant


class ArticleManger:
    url = "https://www.bbc.com/news/articles/cz0nljm4y74o?at_medium=RSS&at_campaign=rss"

    def __init__(self, link):
        self.link = link

    def fetch_url(self):
        article = {}
        if self.url is None:
            return "No Url found!!"
        try:
            response = get(self.url)
            if response.status_code == 200:
                response_text = response.text
                soup = BeautifulSoup(response_text, "html.parser")
                title = soup.find("h1").get_text(strip=True)
                article["title"] = title

                article_phrases = []
                for text_block in soup.find_all(
                    "div", {"data-component": "text-block"}
                ):
                    paragraph = text_block.find_all("p")
                    for phrase in paragraph:
                        phrase_text = phrase.getText(strip=True)
                        article_phrases.append(phrase_text)
                full_article = "\n".join(article_phrases)
                article_object = Article(title, full_article)
                return article_object

            else:
                return "Sorry! failed in fetch full article!!"
        except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    articlemanger = ArticleManger(
        "https://www.bbc.com/news/articles/cz0nljm4y74o?at_medium=RSS&at_campaign=rss"
    )
    article = articlemanger.fetch_url()
    print(article.title)
    print(article.fulltext)
    print("!!!!!!!!!!!!!!!!!!!!!!!!")
    ai_assist = Ai_assistant(article.fulltext)
    print(ai_assist.summarize_article())
    print("AAAAAAAAAAAAAAAAAAAAAAAA")
    print(ai_assist.analize_article())
