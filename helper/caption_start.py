from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extensions import driver
from selenium.webdriver.common.by import By


def caption_tab():
    try:
        # to on captions of google meet
        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.VfPpkd-Bz112c-LgbsSe.fzRBVc.tmJved.xHd4Cb.rmHNDe"))).click()
        print("caption is on and displayed..")
        # element.click()
    except:
        print("caption on, request timeout..")
        driver.quit()
