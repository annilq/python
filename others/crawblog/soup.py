import requests
from bs4 import BeautifulSoup
import pdfkit
from urllib.parse import urlparse  # py3
from settings import Setting

start_url = "https://annilq.github.io/"


class CrawBlog():
    """docstring for CrawBlog"""

    def __init__(self):
        super().__init__()
        self.settings = Setting()
        self.urls = []

    def run(self, url):
        self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
        self.parse_page(url)

    def getUrl(self, url):
        if not url.startswith("https"):
            url = "".join([self.domain, url])  # 补全为全路径
        return url

    # 页面有下一页则抓取下一页
    def get_next_page(self, soup):
        pagination = soup.find(class_="pagination")
        next_btn = pagination.find(class_="next")
        url = next_btn.find("a")["href"]
        self.parse_page(self.getUrl(url))

    def has_next_page(self, soup):
        pagination = soup.find(class_="pagination")
        if pagination:
            next_btn = pagination.find(class_="next")
            if next_btn:
                return True
            else:
                return False
        else:
            return False

    def parse_page(self, start_url):
        response = requests.get(start_url, headers=self.settings.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        # css选择器要有空格
        hrefs = soup.find_all(class_="post-title")
        for href in hrefs:
            url = href.a.get("href")
            self.urls.append(self.getUrl(url))
            # html=requests.get(self.getUrl(url),headers=self.settings.headers)
            # self.parse_body(html)
        if self.has_next_page(soup):
            self.get_next_page(soup)
        else:
            self.parse_body()

    def parse_body(self):
        # print(self.urls)
        pdfkit.from_url(
            self.urls, 'out.pdf', options=self.settings.pdfkit_options)


myblog = CrawBlog()
myblog.run(start_url)