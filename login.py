import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


acccounts = int(len(sys.argv[1:])/2)
print(f'Config {acccounts} accounts')
for i in range(acccounts):
    email = sys.argv[1+i]
    passwd = sys.argv[1+i+acccounts]
    print('----------------------------')

    #1.open browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i+1} loading game...')
    sleep(20)

    #2.input email
    screen = driver.find_element(By.ID, 'layaCanvas')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, -100)\
        .click()\
        .perform()
    driver.find_element(By.NAME, 'input').send_keys(email)
    print('Input email successfully')

    #3.input password
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, -50)\
        .click()\
        .perform()
    driver.find_element(By.NAME, 'input_password').send_keys(passwd)
    print('Input password successfully')

    #4.login
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, 50)\
        .click()\
        .perform()
    print('Entering game...')
    sleep(20) #loading...
    print('Login success')

    # 5.check mails
    print('Check mails')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 350, -210)\
        .click()\
        .perform()
    sleep(5)
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 400, -200)\
        .click()\
        .perform()
    ActionChains(driver)\
        .move_to_element_with_offset(screen,270, -230)\
        .click()\
        .perform()
    ActionChains(driver)\
        .move_to_element_with_offset(screen,50, -220)\
        .click()\
        .perform()
    ActionChains(driver)\
        .move_to_element_with_offset(screen,80, 190)\
        .click()\
        .perform()
    sleep(5)
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 400, -200)\
        .click()\
        .perform()
    sleep(5)
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 400, -200)\
        .click()\
        .perform()
    print('Complete!')
    sleep(5)
    driver.quit()

from datetime import datetime
import time

start_time = time.time()
success = False

try:
    # ... 登录逻辑 ...
    success = True
except Exception as e:
    print("Login failed:", e)
finally:
    execution_time = time.time() - start_time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{current_time}-{'Success' if success else 'Failed'}-{execution_time:.2f}s\n")

