from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

chromeTest = WorkingWithElementsList()
chromeTest.test()