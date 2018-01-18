### 项目依赖

reuqests 用于网络请求，
beautifusoup 用于操作 html 数据
wkhtmltopdf 就是一个非常的工具，它可以用适用于多平台的 html 到 pdf 的转换，pdfkit 是 wkhtmltopdf 的Python封装包。

```python
pip install requests
pip install beautifulsoup4
pip install pdfkit
```

可能遇到的问题
1. 字体小可能是dpi设置问题
2. 字体乱码可能是设置了头部压缩或者字符编码的问题
```
'custom-header': [('Accept-Encoding', 'gzip')],
'encoding': "UTF-8",
'dpi': "300"
```
[参考链接](https://github.com/lzjun567/crawler_html2pdf)
