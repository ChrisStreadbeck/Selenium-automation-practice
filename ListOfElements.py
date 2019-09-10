from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("ClassName -> List Size: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName -> List Size: " + str(length2))

chromeTest = ListOfElements()
chromeTest.test()