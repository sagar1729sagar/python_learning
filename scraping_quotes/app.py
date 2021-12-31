from selenium import webdriver
# import requests

from scraping_quotes.pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
chrome.get("http://quotes.toscrape.com/search.aspx")
# page_content = requests.get("http://quotes.toscrape.com").content

page = QuotesPage(chrome)

author = input("Enter the author name")
page.select_author(author)
tags = page.get_available_tags()
print("Select one of these tags:[{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag : ")
page.select_tag(selected_tag)