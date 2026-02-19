from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button_for_different_languages(browser):
    browser.get(link)
    time.sleep(5)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) == 1, 'Amount of buttons found is incorrect'
