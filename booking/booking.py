import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="C:/selenium_drivers/chromedriver_win32", teardown=False):
        self.driver_path = driver_path
        os.environ['PATH'] = driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    #method to handle changing currency
    def change_currency(self, currency=None):
        #target button using attribute
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        ) 
        currency_element.click()

        #target <a> tag using attribute, change value using method parameters
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, f"a[data-modal-header-async-url-param*='selected_currency={currency}']"
        )
        selected_currency_element.click()
    
    def search_location(self, text):
        search_bar = self.find_element(
            By.ID, 'ss'
        )
        search_bar.clear()
        search_bar.send_keys(text)
        result = self.find_element(
            By.CSS_SELECTOR, f"li[data-i='0']"
        )
        result.click()

    def select_dates(self, leaving, returning):
        leaving_date = self.find_element(
            By.CSS_SELECTOR, f"tr[data-date={leaving}]"
        )
        leaving_date.click()
        returning_date = self.find_element(
            By.CSS_SELECTOR, f"tr[data-data={returning}]"
        )
        returning_date.click()