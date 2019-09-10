from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by ID")

        elementByXPath = driver.find_element(By.XPATH, "//input[@id=\"name\"]")

        if elementByXPath is not None:
            print("We found an element by XPath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

chromeTest = ByDemo()
chromeTest.test()