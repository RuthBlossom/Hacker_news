# Hacker News Article Scraper

## Overview
This Python script scrapes the front page of Hacker News (https://news.ycombinator.com/) to retrieve the titles, links, and upvotes of the top articles. It utilizes the BeautifulSoup library to parse the HTML content of the webpage and extract the relevant information.

![Capture Hacker news](https://github.com/user-attachments/assets/6743e6ab-73d2-465b-85c5-6659d7747a6d)

![Capture hacker news 2](https://github.com/user-attachments/assets/e445dc6b-787c-4eb7-8b31-4916e3bc23a1)



## Prerequisites
- Python 3.x
- BeautifulSoup (`pip install beautifulsoup4`)
- requests (`pip install requests`)

## Usage
1. Run the Python script `hacker_news_scraper.py`.
2. The script will send a GET request to Hacker News and retrieve the HTML response.
3. It will parse the HTML content using BeautifulSoup to extract article titles, links, and upvotes.
4. The details of the article with the maximum upvotes will be printed, including the title, number of upvotes, and link.

## Notes
- Customize the script to suit your needs, such as extracting additional information or performing different analyses on the articles.
- This script demonstrates web scraping techniques using BeautifulSoup and requests to extract data from a specific webpage.
- Be considerate when scraping websites and adhere to their terms of service and usage policies.

## Disclaimer
This project is for educational purposes only. The developer does not bear any responsibility for the misuse of this script for unauthorized activities or any consequences resulting from such misuse.

---
