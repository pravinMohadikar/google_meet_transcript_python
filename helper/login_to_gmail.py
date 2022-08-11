from extensions import driver
from selenium.webdriver.common.by import By


# login to gmail
def gmail_login(email, password):
    
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # input Gmail
    driver.find_element(By.ID, "identifierId").send_keys(email)
    driver.find_element(By.ID, "identifierNext").click()
    driver.implicitly_wait(10)

    # input Password
    driver.find_element(
        "xpath", '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "passwordNext").click()
    driver.implicitly_wait(10)

    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(1)
