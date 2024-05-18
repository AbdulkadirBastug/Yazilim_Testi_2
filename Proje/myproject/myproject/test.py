def test_login_page(driver):
    driver.get("http://127.0.0.1:8000/login/")
    username_field = driver.find_element_by_xpath('//input[@name="username"]')
    password_field = driver.find_element_by_xpath('//input[@name="password"]')
    submit_button = driver.find_element_by_xpath('//button[@type="submit"]')

    username_field.send_keys("test_kullanici")
    password_field.send_keys("sifre")
    submit_button.click()

    # Login sonrası doğrulama
    assert "Dashboard" in driver.title