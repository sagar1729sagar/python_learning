import requests
import logging
import aiohttp
import async_timeout
import asyncio
import time

from scraping_books.pages.all_books_page import AllBooksPage

start_time = time.time()


async def fetch_book(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return response


async def get_multiple_books(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_book(session,url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG, filename='logs.txt')
logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books


# for page_num in range(1, page.page_count):
#     url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
#     page_content = requests.get(url).content
#     logger.debug('Creating AllBooksPage from page content.')
#     page = AllBooksPage(page_content)
#     books.extend(page.books)

loop = asyncio.get_event_loop()
urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(page.page_count)]
page_start = time.time()
loop.run_until_complete(get_multiple_books(loop, *urls))

print(f"Total time : {time.time() - start_time}")
print(f'async total time = {time.time() - page_start}')

