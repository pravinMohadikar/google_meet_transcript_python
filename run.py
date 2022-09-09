from helper.login_to_gmail import gmail_login
from helper.meet_automated import turn_off_mic_cam, join_now, ask_to_join
from helper.caption_start import caption_tab
import time
import os
from extensions import driver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from services.final_transcript_service import final_chat
from random import randint


load_dotenv()

email = os.getenv('Email')
password = os.getenv('Password')

# login to Google account
gmail_login(email, password)

# go to google meet
# driver.get('https://meet.google.com/szw-byqr-sqw')
driver.get('https://meet.google.com/xay-hbhz-iht')

# to turn off mic and cam
turn_off_mic_cam()

# ask_to_join()
join_now()

time.sleep(2)

# to turn on caption
caption_tab()

time.sleep(5)

random_name = randint(000, 9999)
file_name = f'{random_name}.txt'
auth_text = ''
while True:
    try:
        time.sleep(2)
        with open(file_name, "a") as file_object:
            if auth_text != driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML"):
                file_object.write(str(auth_text))
                file_object.write("\n")
            auth_text = driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML")

    except:
        break

final_chat(file_name)
os.remove(file_name)
print("new file saved and temporary text file is removed")
