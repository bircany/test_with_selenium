# Selenium modülünden webdriver sınıfını ve Chrome tarayıcı servisini kullanmak için gerekli olan Service sınıfını içe aktarıyoruz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriver'ın bulunduğu yol için Service sınıfından bir nesne oluşturuyoruz Burada "./chromedriver.exe" ile ChromeDriver dosyasının,
# mevcut çalışma dizininde olduğunu belirtiyoruz
service = Service("./chromedriver.exe")

# Chrome tarayıcısını başlatmak için webdriver sınıfını kullanarak bir Chrome tarayıcı nesnesi oluşturuyoruz
# Bu nesne, yukarıda tanımladığımız Service nesnesi üzerinden ChromeDriver'ı kullanarak Chrome tarayıcısını kontrol eder
driver = webdriver.Chrome(service=service)

# Tarayıcıyı kullanarak belirtilen URL'ye gitmek için get() fonksiyonunu kullanıyoruz
# Bu, Samsun Üniversitesi'nin web sitesini açacaktır
driver.get("http://www.samsun.edu.tr")