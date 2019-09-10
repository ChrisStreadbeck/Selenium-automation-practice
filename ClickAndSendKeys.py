from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        time.sleep(3)

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")

        time.sleep(3)


chromeTest = ClickAndSendKeys()
chromeTest.test()