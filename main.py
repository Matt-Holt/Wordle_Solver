import random
import time
import wordle
from selenium import webdriver
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

rows = driver.find_elements(By.CLASS_NAME, "Row-module_row__dEHfN")
row = 0
next_input = "audio"


def get_row():
    global row
    current_row = rows[row]

    result = ""
    letters = current_row.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")

    for x in letters:
        state = x.get_attribute("data-state")
        if state == "correct":
            result += "G"
        elif state == "present":
            result += "Y"
        else:
            result += "-"

    row += 1
    return result


# Presses each button for each letter in word
def input_word(word):
    word = word.lower()
    if not isinstance(word, str) or len(word) != 5:
        return

    for c in word:
        for b in buttons:
            if c == b.text.lower():
                b.click()

    submit_button.click()
    time.sleep(2)
    result = get_row()
    global next_input
    words = wordle.get_relevant_words(result, word)

    if len(words):
        next_input = random.choice(words)


while row < len(rows):
    input_word(next_input)

