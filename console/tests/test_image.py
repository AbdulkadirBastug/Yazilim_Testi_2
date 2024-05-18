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

class ImageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000")
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("kanla")  # Geçerli bir kullanıcı adı

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("123456789a")  # Geçerli bir şifre

        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()

    def test_image_loaded_index(self):
        driver = self.driver

        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")
    
    def test_image_loaded_blog(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/blog")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")

    def test_image_loaded_industry(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/industry")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")
    
    def test_image_loaded_saveBlog(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/saveBlog")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")

    def test_image_loaded_saveIndustry(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/saveIndustry")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")

    def test_image_loaded_singleBlog(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/singleBlog")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")

    def test_image_loaded_singleIndustry(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/singleIndustyt")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")

    def test_image_loaded_register(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/register")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")
    
    def test_image_loaded_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/login")
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            is_loaded = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", img)
            self.assertTrue(is_loaded, f"Image at {img.get_attribute('src')} failed to load.")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
