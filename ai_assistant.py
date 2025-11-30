from google import genai

from colorama import Fore, Style, init

init()


class Ai_assistant:
    API_Key = "AIzaSyAY3nJbGvpuyCGYKF9DkxnSXk_Ap7Le4r0"
    summary_prompt = """Summarize the following article in four concise bullet points.
    Focus on the main argument and key takeaways."""

    anlaysis_prompt = """You are a Senior News Analyst with 20 years of experience in global media.
      Your tone is objective, professional, and concise. You prioritize facts over sensationalism.
      Your goal is to perform a deep-dive analysis for the follwing article.
      """

    def __init__(self, article, Api_key=API_Key, sum_prompt=summary_prompt):
        self.article = article
        self.api_key = Api_key
        self.summary_prompt = sum_prompt

    def summarize_article(self):

        prompt = f"{self.summarize_article}"
        return self.fetch_ai_model(prompt)

    def analize_article(self):
        prompt = f"{self.anlaysis_prompt}"
        return self.fetch_ai_model(prompt)

    def fetch_ai_model(self, prompt):

        client = genai.Client(api_key=self.api_key)
        prompt = f"""{prompt}\nArticle Start\n{self.article}
        ARTICLE END
        """
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error took place {e}"


if __name__ == "__main__":

    pass
