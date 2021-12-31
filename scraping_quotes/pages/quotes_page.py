from typing import List
from selenium.webdriver.support.ui import Select
from scraping_quotes.locators.quotes_page_locators import QuotesPageLocators
from scraping_quotes.parsers.quote import QuoteParser


class QuotesPage:

    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quote_tags]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)


