**Overview**

This application helps users stay updated by collecting news from multiple sources in one place.
It supports:
RSS feeds
NewsAPI.org
Viewing full articles
Managing feed sources
Searching for topic-based articles
The app converts unstructured data (XML, HTML, JSON) into structured News and Article objects using clean OOP design.

**How to Use** 
1. Run the Application => python main.py
2. Add a Feed => Already a defult exist (BBC News Rss) 
  The app shows all available agencies.
  Choose one or more to add to your feed list. 
3. Fetch News
  Fetches headlines from all your saved feeds.
4. Search By Keyword (NewsAPI)
  Enter a topic → get structured news results.
5. Read Full Article

Paste a URL → get title + full clean article text.
**Future Improvements**
UI version (Tkinter / Web app)
Machine learning topic classification
Automatic summarization
Save articles to reading list
Keyword alerts

 **Features**
✔ RSS Feed Integration

Fetch latest headlines from RSS URLs

Automatically parse entries

Display top articles with color formatting

✔ NewsAPI Integration

Search for news by keyword, date, or category

Convert JSON data into News objects

✔ Feed Repository

Add agency feeds (BBC, CNN, etc.)

Validate new feeds (avoid duplicates)

Delete feeds

Store everything in TinyDB

✔ Article Reader

Fetch full article from link

Extract clean text using BeautifulSoup

Display or return structured article object

✔ Colorized Console Output

Headlines displayed using Colorama

Clear and easy-to-read formatting

✔ Error Handling

Skip invalid URLs

Safe parsing for RSS and JSON

Clear error messages
