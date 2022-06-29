from  selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# search_bar = driver.find_element(By.NAME, "field-keywords")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, "nav-sprite nav-logo-ext nav-progressive-content")
# print(logo.size)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_times[n].text
    }
print(events)
driver.quit()