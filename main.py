from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



def SCAN():
    global tx
    l = len(driver.find_elements(By.XPATH, "/html/body/div/div/main/div/div/div[2]/div"))
    for i in range(1, l):
        if len(driver.find_elements(By.XPATH, f"/html/body/div/div/main/div/div/div[2]/div[{i}]/div[3]/span[1]")) > 0:
            name = driver.find_element(By.XPATH, f"/html/body/div/div/main/div/div/div[2]/div[{i}]/div[3]/span[1]")
            if len(driver.find_elements(By.XPATH, f"/html/body/div/div/main/div/div/div[2]/div[{i}]/div[3]/a")) > 0:
                href = driver.find_element(By.XPATH,
                                           f"/html/body/div/div/main/div/div/div[2]/div[{i}]/div[3]/a").get_attribute(
                    "href")
                print(f"{name.text}: {href}")
                if not f"{name.text}: {href}" in tx:
                    tx += f"{href}\n"
path = r"C:\Users\79879\PycharmProjects\TelegramCryptoCHANELSparcer\chromedriver_win32\chromedriver.exe"
service = Service(executable_path=path)
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
url = "https://combot.org/top/telegram/groups?lng=en&page=1&q=Crypto+pump"
tx = ""


try:
    driver.get(url)
    time.sleep(1)
    html = driver.find_element(By.TAG_NAME, 'html')
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        html.send_keys(Keys.END)
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(0.5)
        if new_height == last_height:
            break
        last_height = new_height
        time.sleep(0.5)
    SCAN()
    time.sleep(10)
except Exception as e:
    print(e)

finally:
    driver.close()
    driver.quit()

print("ВСЕ ДАННЫЕ БЫЛИ УСПЕШНО СПАРШЕНЫ")
with open("result.txt","w", encoding="utf-8") as file:
    file.write(tx)

