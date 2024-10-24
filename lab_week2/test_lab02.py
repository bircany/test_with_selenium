
#Deney No:2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print(" Tarih: ", date, "\n", "Ad Soyad: ", nameWithLastname, "\n",
"Öğrenci Numarası: ", ogrNo, "\n", "Deney No: ", 2);
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#1. Chrome Tarayıcısını Başlatma ve Sayfa Başlığı Alma
#Selenium ile bir Chrome tarayıcısı başlatın ve www.samsun.edu.tr adresine gidin. Sayfanın başlığını alarak ekrana yazdırın.
driver.get("https://www.samsun.edu.tr/")
title = driver.title
time.sleep(2)
print(f"Sayfa Başlığı : {title}")


#2. Birden Fazla Sayfa ile İleri ve Geri Gitme
#Selenium ile Chrome tarayıcısını başlatın ve önce www.samsun.edu.tr, ardından www.google.com adreslerine gidin. Google sayfasına geçtikten sonra geri butonuna basarak
#Samsun Üniversitesi sayfasına geri dönün. Sonra tekrar ileri giderek Google sayfasına dönün.
driver.get("https://www.samsun.edu.tr/") # Samsun Üniversitesi sayfasına git
print("Samsun Üniversitesi sayfasına gidildi.")
time.sleep(3) #3sn bekle
driver.get("https://www.google.com/") # Google sayfasına git
print("Google sayfasına gidildi.")
time.sleep(3) #3sn bekle
driver.back() # Geri git (Samsun Üniversitesi sayfasına geri dön)
print("Geri dönüldü (Samsun Üniversitesi sayfası).")
time.sleep(3) #3sn bekle
driver.forward()  # Tekrar ileri git (Google sayfasına git)
print("İleri gidildi (Google sayfası).")
time.sleep(3) #3sn bekle
driver.quit()



#3.Sayfa Kaynağını Alma ve Kısmi Yazdırma
#https://mf.samsun.edu.tr/sayfasının HTML kaynak kodunu alarak, yalnızca ilk 500 karakterini ekrana yazdırın.
driver.get("https://mf.samsun.edu.tr/")
time.sleep(2)
page_source = driver.page_source
print(page_source[:500])
driver.quit()

#4. Tarayıcı Penceresi Boyutlarını Değiştirme
#Tarayıcıyı başlattıktan sonra varsayılan pencere boyutlarını alın ve ekrana yazdırın.
#Ardından pencere boyutlarını 400x300 olarak ayarlayın ve yeni boyutları kontrol edin.

window_size = driver.get_window_size()
time.sleep(2)
print(f"Default Windows Size: {window_size}")
driver.set_window_size(400, 300)
window_size = driver.get_window_size()
time.sleep(2)
print(f"New Windows Size: {window_size}")
driver.quit()



#5. Sayfa Yenileme ve Başlık Kontrolü
#https://mf.samsun.edu.tr/adresine gidin, sayfayı yenileyin ve sayfa başlığının yenilemeden öncekiyle aynı olup olmadığını kontrol edin.

driver.get("https://mf.samsun.edu.tr/") # Samsun Üniversitesi sayfasına git
title = driver.title
print(f"İlk Sayfa başlığı : {title}")
driver.refresh()
time.sleep(2)
titleNew = driver.title
print(f"Yeni Sayfa başlığı: {titleNew}")

if(titleNew == title):
    print("Title Aynı")
else:
    print("Title aynı değil")
driver.quit()
