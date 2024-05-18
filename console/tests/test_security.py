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

class AccessWithoutLoginTestWithXpath(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:3000/"

    def test_access_without_login_index(self):
        driver = self.driver
        page = "index"
        
        driver.get(self.base_url + page)
            
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']")),
            f"Failed to redirect to login from {page}")
            
        self.assertIn("login", driver.current_url, f"Access to {page} without login should not be permitted.")
    def test_access_without_login_blogSave(self):
        driver = self.driver
        page = "blogSave"
        
        driver.get(self.base_url + page)
           
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']")),
            f"Failed to redirect to login from {page}")
            # URL'in login içerip içermediğini kontrol et
        self.assertIn("login", driver.current_url, f"Access to {page} without login should not be permitted.")

    def test_access_without_login_industrySave(self):
        driver = self.driver
        page = "industrySave"
        
        driver.get(self.base_url + page)
           
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']")),
            f"Failed to redirect to login from {page}")
            # URL'in login içerip içermediğini kontrol et
        self.assertIn("login", driver.current_url, f"Access to {page} without login should not be permitted.")
    
    def test_access_without_login_blog(self):
        driver = self.driver
        page = "blog"
        
        driver.get(self.base_url + page)
            
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']")),
            f"Failed to redirect to login from {page}")
            # URL'in login içerip içermediğini kontrol et
        self.assertIn("login", driver.current_url, f"Access to {page} without login should not be permitted.")

    def test_access_without_login_industry(self):
        driver = self.driver
        page = "industry"
        
        driver.get(self.base_url + page)
           
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']")),
            f"Failed to redirect to login from {page}")
            # URL'in login içerip içermediğini kontrol et
        self.assertIn("login", driver.current_url, f"Access to {page} without login should not be permitted.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
