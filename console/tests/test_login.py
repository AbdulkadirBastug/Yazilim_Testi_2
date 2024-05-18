from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class LoginTestCases(unittest.TestCase):

    def setUp(self):
       
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/login")
        
    def test_valid_login(self):
        driver = self.driver
         
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("kanla")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("123456789a")

        login_button = driver.find_element(By.ID, "login_button")
        login_button.click()

        
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url.rstrip('/') == "http://127.0.0.1:3000/index"
        )

        
        self.assertEqual(driver.current_url.rstrip('/'), "http://127.0.0.1:3000/index")

    def test_invalid_login(self):
        driver = self.driver

        
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("wrong_username")  # Geçersiz bir kullanıcı adı girin

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("wrong_password")  # Geçersiz bir şifre girin

        login_button = driver.find_element(By.ID, "login_button")
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))  
        )

       
        error_message = driver.find_element(By.ID, "message").text
        self.assertIn("Invalid username or password", error_message)

    def test_show_password(self):
        driver = self.driver

       
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("testpassword")

       
        toggle_button = driver.find_element(By.ID, "show-password")
        toggle_button.click()

        self.assertEqual(password_input.get_attribute("type"), "text")

        toggle_button.click()

        self.assertEqual(password_input.get_attribute("type"), "password")


    def test_display_username_with_xpath(self):
        driver = self.driver
       
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("kanla")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("123456789a")

       
        login_button = driver.find_element(By.ID, "login_button")
        login_button.click()

       
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user_display']"))
        )

        
        user_display = driver.find_element(By.XPATH, "//*[@id='user_display']")
        displayed_username = user_display.text
        expected_message = "Welcome Kanla"
        self.assertIn(expected_message, displayed_username, "Kullanıcı adı sayfada doğru bir şekilde görünmüyor.")


    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()