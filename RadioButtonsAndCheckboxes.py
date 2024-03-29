from selenium import webdriver
import time

class RadioButtonsAndCheckboxes():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)
        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)
        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)
        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()

        time.sleep(2)
        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected())) # True if selected, False is not selected
        print("Benz Radio button is selected? " + str(benzRadioBtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz Checkbox is selected? " + str(benzCheckbox.is_selected()))

chromeTest = RadioButtonsAndCheckboxes()
chromeTest.test()
