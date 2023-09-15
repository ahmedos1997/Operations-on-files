# توجد مشكلة تقريبا الاصدار غير متوافق مع الحزم الرجاء تكملة هذذا الدرس بعد الانتهاء من الكورس
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page',)


elem = browser.find_element(By.CSS_SELECTOR, '#mp-tfa > p')
print((elem.text()))



