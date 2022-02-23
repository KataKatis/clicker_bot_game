import threading
from selenium import webdriver
from selenium.webdriver.common.by import By

# start driver and chromedriver.exe
driver = webdriver.Chrome()
driver.get("https://www.tetralark.com/ClickerJs/")

# thread of click me button
clickme_button = driver.find_element(By.XPATH, "//button[text()='Click me']")


def clickme(button, boolean):
    while boolean:
        button.click()

def new_upgrade():
    while True:
        ask = int(input("Which upgrade to you want to improve ? "))-1
        ntimes = int(input("How many times ?"))
        new_upgrade = driver.find_element(By.CSS_SELECTOR, f"button[data-reactid='.0.3.0.${ask}.${ask}.${ask}']")
        thread = threading.Thread(target=buy_upgrade, args=(new_upgrade, ntimes))
        thread.start()


thread = threading.Thread(target=clickme, args=(clickme_button, True))
thread.start()

thread = threading.Thread(target=new_upgrade)
thread.start()


def buy_upgrade(upgrade_button, times):
    actual = 0
    while actual < times:
        try:
            if upgrade_button.is_enabled():
                upgrade_button.click()
                actual += 1
        except:
            continue
    #  boolean:
    #     upgrade_button.click()


# buy upgrades
upgrade_number = 0

while True:  # .0.3.0.$x.$x.$x

    try:
        upgrade = driver.find_element(By.CSS_SELECTOR, f"button[data-reactid='.0.3.0.${upgrade_number}.${upgrade_number}.${upgrade_number}']")
        upgrade.click()
        thread = threading.Thread(target=buy_upgrade, args=(upgrade, 1000))
        thread.start()
        upgrade_number += 1

    except:
        continue

print("GOOD !")
input()

driver.quit()
