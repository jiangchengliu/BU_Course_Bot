from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#This will leave browser opne after script is finished
options = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                          options=options)

#navigates to the website 
driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1681937313?ModuleName=final_exam.pl")

driver.find_element(By.ID, "").send_keys()
driver.find_element(By.ID, "")
driver.find_element(By.CLASS_NAME, 'input-submit').click()






