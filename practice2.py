from selenium import webdriver
from selenium.webdriver.common.by import By

class Practice2():

    def test(self):
        baseUrl = "http://dhtmlx.com/docs/products/dhtmlxGrid/"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)


# Exercise 2:
# http://dhtmlx.com/docs/products/dhtmlxGrid/
# Find the name of an owner

        owner = driver.find_element(By.XPATH, "//*[@id=\"grid-demo\"]/div/div[2]/div/div[2]/div[1]/div[3]/div[4]/div")
        print('Owner is: ', owner.text)

chromeTest = Practice2()
chromeTest.test()