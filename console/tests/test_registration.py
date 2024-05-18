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
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile,unittest,uuid


class RegistrationTestCases(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000")  
        self.img_size=(600,438)
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("kanla")  # Geçerli bir kullanıcı adı

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("123456789a")  # Geçerli bir şifre

        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()


        # Geçici bir görüntü dosyası oluştur
        self.temp_image = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        image = Image.new('RGB', (100, 100), color = 'red')
        image.save(self.temp_image.name)

    def test_successful_saveBlog(self):
        driver = self.driver

        
        saveBlog = self.driver.find_element(By.ID, "saveBlog")
        saveBlog.click()

        unique_suffix = uuid.uuid4().hex[:6]  
        title = f"Test Blog {unique_suffix}"
        content = "This is a test blog content."
        

        
        title_input = driver.find_element(By.ID, "title")
        content_input = driver.find_element(By.ID, "content")
        image_input = driver.find_element(By.ID, "image")
        
        
        title_input.send_keys(title)
        content_input.send_keys(content)
        image_input.send_keys(self.temp_image.name)
    
       
        saveBlog_button = driver.find_element(By.ID, "saveBlog_button")
        saveBlog_button.click()
        
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
        expected_message = "Blog post saved successfully!"
        self.assertEqual(success_message.text, expected_message, "Kayıt sonrası mesaj yanlış veya görüntülenmiyor.")
        
        

    def test_successful_saveIndustry(self):
        driver = self.driver

        
        saveIndustry = self.driver.find_element(By.ID, "saveIndustry")
        saveIndustry.click()

        unique_suffix = uuid.uuid4().hex[:6]  
        name = f"user_{unique_suffix}"
        content = "This is a industry content."
       
        

        
        name_input = driver.find_element(By.ID, "name")
        content_input = driver.find_element(By.ID, "content")
        image_input = driver.find_element(By.ID, "image")

        
        name_input.send_keys(name)
        content_input.send_keys(content)
        image_input.send_keys(self.temp_image.name)

       
        saveIndustry_button = driver.find_element(By.ID, "saveIndustry_button")
        saveIndustry_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
        expected_message = "Industry saved successfully!"
        self.assertEqual(success_message.text, expected_message, "Kayıt sonrası mesaj yanlış veya görüntülenmiyor.")

        
        

    def test_duplicate_title_xpath(self):
        driver = self.driver
        
        driver.get("http://127.0.0.1:3000/blogSave")

        
        title=f"BlogTitle_{uuid.uuid4().hex}"

        for _ in range(2):
            title_input = driver.find_element(By.ID, "title")
            title_input.clear()
            title_input.send_keys(title)
            content_input = driver.find_element(By.ID, "content")
            content_input.send_keys("Test content for duplicate title")
            image_input = driver.find_element(By.ID, "image")
            image_input.clear()
            image_input.send_keys(self.temp_image.name)
            save_button = driver.find_element(By.ID, "saveBlog_button")
            save_button.click()

            # İlk deneme başarılı olmalı, ikinci deneme hata mesajı göstermeli
            if _ == 1:  # İkinci denemede
                error_message = driver.find_element(By.XPATH, "//div[@id='message']")
                self.assertIn("Title is already exists.", error_message.text)

    def test_duplicate_name_xpath(self):
        driver = self.driver
        
        driver.get("http://127.0.0.1:3000/industrySave")

        # Aynı title'ı iki kez kaydetmeye çalış
        name = f"InsutryName_{uuid.uuid4().hex}"  
        #title="Dublicate Title"

        for _ in range(2):
            name_input = driver.find_element(By.ID, "name")
            name_input.clear()
            name_input.send_keys(name)
            content_input = driver.find_element(By.ID, "content")
            content_input.send_keys("Test content for duplicate name")
            image_input = driver.find_element(By.ID, "image")
            image_input.clear()
            image_input.send_keys(self.temp_image.name)
            save_button = driver.find_element(By.ID, "saveIndustry_button")
            save_button.click()

            # İlk deneme başarılı olmalı, ikinci deneme hata mesajı göstermeli
            if _ == 1:  # İkinci denemede
                error_message = driver.find_element(By.XPATH, "//div[@id='message']")
                self.assertIn("Industry is already exists.", error_message.text)
    
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
