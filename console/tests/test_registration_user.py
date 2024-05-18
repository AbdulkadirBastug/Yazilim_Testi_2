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
import uuid,unittest

class RegistrationUserTestCases(unittest.TestCase):

    def setUp(self):
        # Chrome WebDriver'ını başlat
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/register")  # Kayıt sayfasına git

    def test_successful_registration(self):
        driver = self.driver

        unique_suffix = uuid.uuid4().hex[:6]  # Benzersiz bir suffix oluştur
        username = f"user_{unique_suffix}"
        email = f"user_{unique_suffix}@example.com"
        # Kullanıcı bilgileri alanlarını bul
        username_input = driver.find_element(By.ID, "username")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        # Test kullanıcı bilgileri gir
        username_input.send_keys(username)
        email_input.send_keys(email)
        password_input.send_keys("validPassword123")

        # Kayıt ol butonunu bul ve tıkla
        register_button = driver.find_element(By.ID, "register_button")
        register_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
        expected_message = "Registration successful. Please log in."
        self.assertEqual(success_message.text, expected_message, "Kayıt sonrası mesaj yanlış veya görüntülenmiyor.")

    def test_failed_registration_due_to_existing_username(self):
        driver = self.driver
        existing_username = "kanla"  
        email = "newuser@example.com"

        # Kullanıcı bilgileri alanlarını bul
        username_input = driver.find_element(By.ID, "username")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        # Test kullanıcı bilgileri gir
        username_input.send_keys(existing_username)
        email_input.send_keys(email)
        password_input.send_keys("validPassword123")
       
        # Kayıt ol butonunu bul ve tıkla
        register_button = driver.find_element(By.ID, "register_button")
        register_button.click()

        # Hata mesajını kontrol et
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
        expected_error = "Username is already taken"
        self.assertIn(expected_error, error_message.text, "Kullanıcı adı zaten alınmış hatası verilmedi.")
    
    def test_failed_registration_due_to_existing_email(self):
        driver = self.driver
        username = "newusername"  
        existing_email = "kadir5538@gmail.com"

        # Kullanıcı bilgileri alanlarını bul
        username_input = driver.find_element(By.ID, "username")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        # Test kullanıcı bilgileri gir
        username_input.send_keys(username)
        email_input.send_keys(existing_email)
        password_input.send_keys("validPassword123")
       
        # Kayıt ol butonunu bul ve tıkla
        register_button = driver.find_element(By.ID, "register_button")
        register_button.click()

        # Hata mesajını kontrol et
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
        expected_error = "Email is already registered"
        self.assertIn(expected_error, error_message.text, "Kullanıcı adı zaten alınmış hatası verilmedi.")

    def test_invalid_email_registration(self):
        driver = self.driver
        invalid_email = "invalid-email"

        # Kullanıcı bilgileri alanlarını bul
        username_input = driver.find_element(By.ID, "username")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        # Test kullanıcı bilgileri gir
        username_input.send_keys("newuser")
        email_input.send_keys(invalid_email)
        password_input.send_keys("validPassword123")

        
        register_button = driver.find_element(By.ID, "register_button")
        register_button.click()

        
        WebDriverWait(driver, 10).until(
            lambda driver: email_input.get_attribute('validationMessage') != ''
        )

        # Hata mesajını doğrula
        self.assertNotEqual(email_input.get_attribute('validationMessage'), '', "Geçersiz e-posta adresi için uyarı mesajı yok.")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
