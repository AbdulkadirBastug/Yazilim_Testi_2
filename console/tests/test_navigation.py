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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NavigationTest(unittest.TestCase):
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/login")  

        # Giriş yapma işlemi
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("kanla")  # Geçerli bir kullanıcı adı

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("123456789a")  # Geçerli bir şifre

        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()
        
    

    def test_blog_navigation(self):
        driver = self.driver

        
        blog_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "blog")),
            "Blog link not found on page"
        )
        blog_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("blog"),
            "Did not navigate to Blog page"
        )
        self.assertIn("blog", driver.current_url, "URL does not include 'blog'")

    def test_industry_navigation(self):
        driver = self.driver

        
        industry_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "industry")),
            "Industry link not found on page"
        )
        industry_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("industry"),
            "Did not navigate to Industry page"
        )
        self.assertIn("industry", driver.current_url, "URL does not include 'industry'")

    def test_save_blog_navigation(self):
        driver = self.driver

        
        save_blog_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Save Blog Post")),
            "Save Blog Post link not found on page"
        )
        save_blog_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("blogSave"),
            "Did not navigate to Save Blog Post page"
        )
        self.assertIn("blogSave", driver.current_url, "URL does not include 'blogSave'")

    def test_save_industry_navigation(self):
        driver = self.driver

      
        save_industry_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Save Industry")),
            "Save Industry link not found on page"
        )
        save_industry_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("industrySave"),
            "Did not navigate to Save Industry page"
        )
        self.assertIn("industrySave", driver.current_url, "URL does not include 'industrySave'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
