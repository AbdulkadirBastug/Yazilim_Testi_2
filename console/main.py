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
import os

def load_tests(loader):
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('tests', pattern='test_*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

def main():
    print("Test Senaryoları Menüsü")
    print("1- Tüm Testleri Çalıştır")
    print("2- Login Testleri")
    print("3- Navigation Testleri")
    print("4- Blog ve Industry Kayıt Testleri")
    print("5- Resim Yükleme Testleri")
    print("6- Session Testleri(5 dk sürer!!)")
    print("7- Kullanıcı Kayıt Testleri")
    print("8- Security Testleri")
    print("9- Çıkış Yap")

    choice = input("Lütfen çalıştırmak istediğiniz test numarasını girin: ")

    if choice == '1':
        
        test_loader = unittest.TestLoader()
        test_suite = load_tests(test_loader)
        runner = unittest.TextTestRunner()
        runner.run(test_suite)
    elif choice == '2':
        os.system("python -m unittest tests/test_login.py")
    elif choice == '3':
        os.system("python -m unittest tests/test_navigation.py")
    elif choice == '4':
        os.system("python -m unittest tests/test_registration.py")
    elif choice == '5':
        os.system("python -m unittest tests/test_image.py")
    elif choice == '6':
        os.system("python -m unittest tests/test_session.py")
    elif choice == '7':
        os.system("python -m unittest tests/test_registration_user.py")
    elif choice == '8':
        os.system("python -m unittest tests/test_security.py")
    elif choice == '9':
        print("Çıkış yapılıyor.")
        return
    else:
        print("Geçersiz seçim.")

if __name__ == '__main__':
    main()
