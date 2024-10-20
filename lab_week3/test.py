from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print(f"DENEY NO : 3 "+"\n Tarih : 11.10.2024 \n" + " Ad Soyad : Bircan Yılmaz "+"\nÖğrenci numarası : 241478092")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/birca/OneDrive/Desktop/deneme.html")
time.sleep(2)

#
learn_more_button = driver.find_element(By.ID, "learn-more-btn")
learn_more_button.click()
time.sleep(3)
print("Bircan Yılmaz")
print("Learn More butonuna tıklandı.")


#
name_input = driver.find_element(By.ID, "name")
name_input.send_keys("Bircan Yılmaz")
time.sleep(3)
print("İsim girildi.")

#
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("241478092@samsun.edu.tr")
time.sleep(3)
print("Email girildi.")

#
message_textarea = driver.find_element(By.ID, "message")
message_textarea.send_keys("Bu Bircan Yılmaz'ın örnek bir mesajıdır.")
time.sleep(2)
print("Mesaj girildi.")

#
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
print("Form gönderildi.")
time.sleep(3)
driver.get("file:///C:/Users/birca/OneDrive/Desktop/deneme.html")

#
about_link = driver.find_element(By.LINK_TEXT, "About")
about_link.click()
print("About bölümüne gidildi.")
time.sleep(3)
#
email_link = driver.find_element(By.LINK_TEXT, "241478092@samsun.edu.tr")
assert email_link.get_attribute("href") == "mailto:241478092@samsun.edu.tr"
print("Email link doğrulandı.")
time.sleep(3)

driver.quit()
