import requests
from bs4 import BeautifulSoup

start_url = "http://annilq.github.io/"
urls = []

class CrawBlog():
    """docstring for CrawBlog"""

    def __init__(self, url):
        super().__init__()
        self.url = url

    def function():
        pass

    # 页面有下一页则抓取下一页
    def get_next_page(soup):
        pagination = soup.find(class_="pagination")
        if pagination:
            next_btn = pagination.find(class_="next")
            if next_btn:
                url = next_btn.find("a")["href"]
                parse_page(start_url + url)

    def parse_page(start_url):
        response = requests.get(start_url)
        soup = BeautifulSoup(response.content, "html.parser")
        # css选择器要有空格
        hrefs = soup.find_all(class_="post-title")
        urls.append(hrefs)
        for href in hrefs:
            url = href.a.get("href")
        get_next_page(soup)


myblog = CrawBlog(start_url)
# parse_page(start_url)
