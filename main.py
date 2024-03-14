# Importing necessary libraries
from bs4 import BeautifulSoup
import requests

# Sending a GET request to Hacker News website and getting the HTML response
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Lists to store article titles, links, and upvotes
article_titles = []
article_links = []
article_upvotes = []

# Extracting article titles and links
for article_tag in soup.find_all(name="span", class_="titleline"):
    # Appending the text content of the span (article title) to the list
    article_titles.append(article_tag.getText())
    # Appending the 'href' attribute of the 'a' tag (article link) to the list
    article_links.append(article_tag.find("a")["href"])

# Extracting article upvotes
for article in soup.find_all(name="td", class_="subtext"):
    # Checking if the 'score' class is present (indicating upvotes)
    if article.span.find(class_="score") is None:
        # If not present, appending 0 to the list (no upvotes)
        article_upvotes.append(0)
    else:
        # If present, extracting the upvotes and converting to integer
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# Finding the index of the article with the maximum upvotes
max_points_index = article_upvotes.index(max(article_upvotes))

# Printing the details of the article with the maximum upvotes
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)
