from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.explicit_wait_type import ExplicitWaitType
import time

class ExplicitWaitDemo():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2019")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        time.sleep(2)
        returnDate.clear()
        returnDate.send_keys("12/26/2019")
        driver.find_element(By.XPATH, "//*[@id=\"gcw-flights-form-hp-flight\"]/div[8]/label/button").click()

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

chromeTest = ExplicitWaitDemo()
chromeTest.test()