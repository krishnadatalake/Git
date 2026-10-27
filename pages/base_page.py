class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")
        return self
