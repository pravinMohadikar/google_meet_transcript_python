from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')

opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
print(webdriver.Chrome)
driver = webdriver.Chrome(options=opt)

