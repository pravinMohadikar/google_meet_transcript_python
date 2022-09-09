from extensions import driver
import time
from selenium.webdriver.common.by import By


def turn_off_mic_cam():
    # turn off Microphone
    time.sleep(1)
    driver.find_element("xpath",
                        '//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]').click()
    driver.implicitly_wait(10)

    # turn off camera
    time.sleep(1)
    driver.find_element("xpath",
                        '//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]').click()
    driver.implicitly_wait(10)


def join_now():
    # Join meet
    print(1)
    time.sleep(1)
    driver.implicitly_wait(10)
    driver.find_element("xpath",
                        '//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button').click()
    driver.implicitly_wait(10)
    print(1)


def ask_to_join():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(20)
    driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths

