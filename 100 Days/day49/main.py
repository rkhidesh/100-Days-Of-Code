from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    "https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Canada&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

time.sleep(2)
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys("rebeccakhidesheli@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("ilovesummer14")

sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.send_keys(Keys.ENTER)

job = driver.find_element(By.XPATH, '//*[@id="ember213"]')
job.send_keys(Keys.ENTER)

save_job = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
save_job.send_keys(Keys.ENTER)