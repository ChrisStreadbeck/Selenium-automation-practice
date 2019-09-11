from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test(self):
        baseUrl = "http://www.southwest.com"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        cityField.clear()
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//ul[@id='LandingAirBookingSearchForm_originationAirportCode']//li[contains(text(),'NJ - EWR')]")
        itemToSelect.click()

        time.sleep(3)
        driver.quit()

chromeTest = AutoComplete()
chromeTest.test()