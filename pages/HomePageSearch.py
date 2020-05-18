from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PracticeHomePageSearch:
    url_togo = "http://automationpractice.com/index.php"
    search_input = (By.ID, "search_query_top")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.url_togo)

    def search(self, search_phrase):
        search_input = self.browser.find_element(*self.search_input)
        search_input.send_keys(search_phrase + Keys.RETURN)
