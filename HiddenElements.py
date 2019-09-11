from selenium import webdriver
import time

class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        # Find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Added code to scroll up because the element was hiding behind the top navigation menu
	# You will learn about scrolling in future lecture
        driver.execute_script("window.scrollBy(0, -150);")
        # Click the Show button
        driver.find_element_by_id("show-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)
        # Browser Close
        driver.quit()

    def testExpedia(self):
        baseUrl = "http://www.expedia.com"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.find_element_by_id("tab-flight-tab-hp").click()

        drpdwnElement = driver.find_element_by_id("flight-age-select-1-hp-flight")
        print("Element visible? " + str(drpdwnElement.is_displayed()))


chromeTest = HiddenElements()
chromeTest.testLetsKodeIt()
chromeTest.testExpedia()