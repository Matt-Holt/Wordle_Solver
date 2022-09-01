import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

url = "https://www.nytimes.com/games/wordle/index.html"
driver = webdriver.Chrome("D:\\Chromedriver.exe")
driver.get(url)

# Maximises window
driver.maximize_window()

# Clicks reject cookies
driver.find_element(By.XPATH, '//*[@id="pz-gdpr-btn-reject"]').click()
# Closes hint menu
driver.find_element(By.XPATH, '//*[@id="wordle-app-game"]/div[3]/div/div').click()

# Adds all buttons to array
buttons = driver.find_elements(By.CLASS_NAME, "Key-module_key__Rv-Vp")
submit_button = driver.find_element(By.XPATH, '//*[@id="wordle-app-game"]/div[2]/div[3]/button[1]')


# Presses each button for each letter in word
def input_word(word):
    word = word.upper()
    if not isinstance(word, str) or len(word) != 5:
        return

    for c in word:
        for b in buttons:
            if c == b.text.upper():
                try:
                    b.click()
                except ExceptionGroup:
                    print("Button cannot be clicked for some reason")

    submit_button.click()


input_word("Hello")
time.sleep(2)
input_word("Hello")
time.sleep(2)
input_word("Hello")
time.sleep(2)
input_word("Hello")
time.sleep(2)
input_word("Hello")
time.sleep(2)
input_word("Hello")
