from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time
list = "https://proyecto-cintianecol.web.app/,https://pov-portfolio.web.app/,https://portfolio-karinsd.web.app/"
tab = ","
set = 120

list = list.split(tab)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

while True:
	for i in list:
		print(i)
		driver.get(i)
		time.sleep(set)