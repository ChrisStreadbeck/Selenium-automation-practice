from selenium import webdriver
from selenium.webdriver.common.by import By

class Practice1():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)


# Exercise 1:
# "https://learn.letskodeit.com/p/practice"
# Find the price of the course “Python Programming Language”

        pythonPrice = driver.find_element(By.XPATH, "//*[@id=\"product\"]/tbody/tr[3]/td[3]")
        print("the python course price is: " + pythonPrice.text)

chromeTest = Practice1()
chromeTest.test()