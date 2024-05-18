# /****************************************************************************
# **					SAKARYA ÜNİVERSİTESİ
# **			     BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
# **				    BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
# **				        YAZILIM TESTİ
# **
# **				ÖDEV NUMARASI…...: 2
# **				ÖÐRENCÝ ADI...............: Abdulkadir Baştuğ
# **				ÖÐRENCÝ NUMARASI.: B201210084
# **				DERS GRUBU…………: A
# ****************************************************************************/
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SessionTimeoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:3000/"
        self.login()

    def login(self):
        self.driver.get(self.base_url + "login")
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("kanla")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("123456789a")
        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()
        

    def test_session_timeout(self):
        # Oturum süresi sonunda test yapmak için belirlenen süre kadar bekleyin
        time.sleep(300)  # Örneğin, oturum süresi 5 dakika sonra doluyor
        
       
        self.driver.get(self.base_url + "blog")
        
       
        WebDriverWait(self.driver, 10).until(EC.url_contains("login"), "Should redirect to login page after session timeout")
        
        # Giriş sayfasında olup olmadığını doğrulayın
        self.assertTrue("login" in self.driver.current_url, "User should be redirected to login page after session expires")

    def test_logout_process_xpath(self):
        # Logout butonunu bul ve tıkla
        logout_button = self.driver.find_element(By.XPATH, "//a[@href='/logout/']")
        logout_button.click()

        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("login"),
            "Logout failed or the login page did not load after logout"
        )
        
        # Giriş sayfasında olup olmadığını kontrol et
        self.assertIn("login", self.driver.current_url, "User is not on the login page after logout.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
