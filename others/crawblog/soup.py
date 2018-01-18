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
        print(self.urls)
        pdfkit.from_url(
            self.urls, 'out.pdf', options=self.settings.pdfkit_options)


myblog = CrawBlog()
# myblog.run(start_url)

lists = [
    'https://annilq.github.io/2017/12/18/pwa/',
    'https://annilq.github.io/2017/12/07/serach/',
    'https://annilq.github.io/2017/12/01/sort/',
    'https://annilq.github.io/2017/11/29/datastructures/',
    'https://annilq.github.io/2017/11/09/rxjs/',
    'https://annilq.github.io/2017/10/11/observable-pattern/',
    'https://annilq.github.io/2017/10/11/Promise/',
    'https://annilq.github.io/2017/09/28/generator/',
    'https://annilq.github.io/2017/07/16/build-your-redux/',
    'https://annilq.github.io/2017/07/08/python-todo/',
    'https://annilq.github.io/2017/07/02/async/',
    'https://annilq.github.io/2017/04/09/nodejs/',
    'https://annilq.github.io/2017/03/27/native/',
    'https://annilq.github.io/2017/03/22/atom/',
    'https://annilq.github.io/2016/11/15/ios-tip/',
    'https://annilq.github.io/2016/10/15/emitter/',
    'https://annilq.github.io/2016/04/18/mongoDb/',
    'https://annilq.github.io/2016/01/07/Cordovarelease/',
    'https://annilq.github.io/2015/12/25/hexo-start/'
]
pdfkit.from_url('https://annilq.github.io/2017/12/18/pwa/', 'out.pdf', options=myblog.settings.pdfkit_options)
