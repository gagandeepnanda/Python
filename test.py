from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://myte.accenture.com")
user = "gagan.deep.nanda"
pwd = "Chutiya3#"
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'userNameInput')))
elem = driver.find_element_by_id("userNameInput")
elem.send_keys(user)
elem = driver.find_element_by_id("passwordInput")
elem.send_keys(pwd)
elem = driver.find_element_by_id("submitButton")
elem.click()
wait = WebDriverWait(driver, 30)
element = wait.until(EC.element_to_be_clickable((By.ID, 'vipOoblink')))
elem = driver.find_element_by_id("vipOoblink")
elem.click()
elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/form/div[1]/label[2]/input")
elem.click()
elem = driver.find_element_by_id("vipSend")
elem.click()
driver.implicitly_wait(1000)
elem = driver.find_element_by_xpath("//*[@id='vipSubmitOTP']")
elem.click()
wait = WebDriverWait(driver, 300)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_MainContentPlaceHolder_AnnouncementControl_lnk_Enter2"]')))
element.click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_MainContentPlaceHolder_Expense-IN"]')))
element.clikck()
wait = WebDriverWait(driver, 400)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_MainContentPlaceHolder_ContentPlaceHolder_TimeReport_Checkbox"]')))
