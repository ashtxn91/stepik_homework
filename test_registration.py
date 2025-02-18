import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.link = "https://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

    def test_registration(self):
        input_name = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
        input_name.send_keys('Adolf')
        input_email = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input_email.send_keys('email@email.netzx')

        button = self.browser.find_element(By.XPATH, "/html/body/div/form/button")
        button.click()

        # Используем WebDriverWait вместо time.sleep
        welcome_text_elt = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/h1"))
        )
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
