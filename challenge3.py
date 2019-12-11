import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3forloop(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        for element in elements:
            print(element.text + " - " + element.get_attribute("href"))

    def test_challenge3whileloop(self): # Get the name and the a track
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
        i = 0
        while i < len(elements):
            print(elements[i].text + " - " + elements[i].get_attribute("href"))
            i += 1


if __name__ == '__main__':
    unittest.main()