from selenium import webdriver
# import requests

from scraping_quotes.pages.quotes_page import QuotesPage,InvalidTagForAuthorError


try:
    author = input("Enter the author name")
    tag = input("Enter your tag : ")

    chrome = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
    chrome.get("http://quotes.toscrape.com/search.aspx")
    # page_content = requests.get("http://quotes.toscrape.com").content

    page = QuotesPage(chrome)


    # page.select_author(author)
    # tags = page.get_available_tags()
    # print("Select one of these tags:[{}]".format(" | ".join(tags)))

    # page.select_tag(selected_tag)
    # page.search_button.click()

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error has occurred.Please try again")


