from selenium import webdriver

class FindByElement():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        driver.maximize_window()

        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by ID")

        elementByName = driver.find_element_by_name("enter-name")

        if elementByName is not None:
            print("We found an element by Name")

        elementByXPath = driver.find_element_by_xpath("//input[@id=\"name\"]")

        if elementByXPath is not None:
            print("We found an element by XPath")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print("We found an element by CSS")

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Logi")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")

        elementByClassName = driver.find_element_by_class_name("inputs")

        if elementByClassName is not None:
            print("We found an element by Class")
                    
        elementByTagName = driver.find_element_by_tag_name("h1")

        if elementByTagName is not None:
            print("We found an element by Tag")


chromeTest = FindByElement()
chromeTest.test()