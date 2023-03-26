from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time

list = "https://proyecto-cintianecol.web.app/,https://pov-portfolio.web.app/,https://portfolio-karinsd.web.app/,https://portfolioale-17e1a.web.app/,https://nuevoivonportf.web.app/,https://portfoliofrontend-37881.web.app/,https://porfolio-black-storm.web.app/,https://portfolio-alvaro.web.app/,https://porfolio-ap-ljm.web.app/,https://portfoliojaviertoro.web.app/intro,https://nacargentinaprograma.web.app/,https://portfolio-frontend-nicolas.web.app/,https://portfolio-ezniev.web.app/,https://portfolioelkebarrios.web.app/,https://portfolio-frontend-melinda.web.app/"
tab = ","
set = 120
list = list.split(tab)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

while True:
	for i in list:
		print(i)
		driver.get(i)
		time.sleep(set)
