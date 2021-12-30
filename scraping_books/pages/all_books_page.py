import re
import logging
from bs4 import BeautifulSoup
from scraping_books.locators.all_books import AllBooksPageLocators
from scraping_books.parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self,page_content):
        logger.debug('Parsing page contnet with beautifulsoup')
        self.soup = BeautifulSoup(page_content,'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in page using {AllBooksPageLocators.BOOKS} ')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`')
        return pages