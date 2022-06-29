from  selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.ca/Microsoft-RRS-00001-Xbox-Series-S/dp/B08G9J44ZN/ref=sr_1_9/ref=GM22_3?pf_rd_r=A69AA2CYZJZCK62Y13V9&pf_rd_p=33e99f85-5218-4306-89df-f14bf0af4d96&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=top-slot-1&pf_rd_t=&pf_rd_i=&_encoding=UTF8&brr=1&pd_rd_r=f0634ee3-425c-4c5d-a5a6-2b8a29a5239e&pd_rd_w=dzoD9&pd_rd_wg=FmnFu&pf_rd_p=110291c5-558c-4e37-9cc9-ac65b1ccefbc&pf_rd_r=EH9YEE31DAHB69RKEKTA&qid=1652747584&rd=1&s=videogames&sr=1-9")

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)
driver.quit()