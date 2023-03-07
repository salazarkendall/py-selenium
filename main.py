import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
time.sleep(2)

# Open page
driver.get('https://practicetestautomation.com/practice-test-login/')
time.sleep(2)

# Type username student into Username field
username_locator = driver.find_element(
    by=By.ID, value="username")
username_locator.send_keys('student')

# Type password Password123 into Password field
password_locator = driver.find_element(
    by=By.ID, value="password")
password_locator.send_keys('Password123')

# Push Submit button
submit_button_locator = driver.find_element(
    by=By.XPATH, value="//button[@id='submit']")
submit_button_locator.click()
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
current_url = driver.current_url
assert current_url == 'https://practicetestautomation.com/logged-in-successfully/'

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(
    by=By.TAG_NAME, value="h1")
current_text = text_locator.text
assert current_text == "Congratulations" or current_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_button_locator = driver.find_element(
    by=By.LINK_TEXT, value="Log out")
assert logout_button_locator.is_displayed()
