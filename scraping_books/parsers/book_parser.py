import re
import logging
from scraping_books.locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name},£{self.price},{self.rating}-{"star" if self.rating == 1 else "stars"}>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        return self.parent.select_one(BookLocators.NAME_LOCATOR).attrs['title']

    @property
    def link(self):
        logger.debug('Finding book link...')
        return self.parent.select_one(BookLocators.LINK_LOCATOR).attrs['href']

    @property
    def price(self):
        logger.debug('Finding book price...')
        pattern = '£([0-9]+\.[0-9]+)'
        return float(re.search(pattern, self.parent.select_one(BookLocators.PRICE_LOCATOR).string).group(1))

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        classes = self.parent.select_one(BookLocators.RATING_LOCATOR).attrs['class']
        rating = [c for c in classes if c != 'star-rating'][0]
        return BookParser.RATINGS.get(rating, "No rating Found")
