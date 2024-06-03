from selenium import webdriver
import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.ie.options import Options as ieo
from selenium.webdriver.chrome.options import Options as cho


class WebDriverFactory:

    def __init__(self, browser) -> None:
        self.browser = browser

    def getWebDriverInstance(self) -> WebDriver | WebDriver | WebDriver:
        baseURL = "https://www.barchart.com/cmdty/data/fundamental/explore"

        options = cho()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            cService = webdriver.ChromeService(
                executable_path=f"{os.getcwd()}/chromedriver.exe"
            )
            driver = webdriver.Chrome(service=cService)
        else:
            # driver = webdriver.Chrome(options=opt)
            driver = webdriver.Chrome()

        # driver.implicitly_wait(5)
        # driver.set_page_load_timeout(30)
        # driver.maximize_window()
        driver.get(baseURL)

        return driver
