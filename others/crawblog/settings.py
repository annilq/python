options = {
    'page-size':
    'Letter',
    'margin-top':
    '0.75in',
    'margin-right':
    '0.75in',
    'margin-bottom':
    '0.75in',
    'margin-left':
    '0.75in',
    'encoding':
    "UTF-8",
    'custom-header': [('Accept-Encoding', 'gzip')],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'outline-depth':
    10,
}
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

headers = {
    "accept":
    "text/html,application/xhtml+xml,application/xml",
    "accept-language":
    "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control":
    "no-cache",
    "connection":
    "keep-alive",
    "user-agent":
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}


class Setting(object):
    """docstring for Setting"""

    def __init__(self):
        super().__init__()
        self.headers = headers
        self.pdfkit_options = options