import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# + FILL THE PATH OF THE CHROME DRIVER

PATH = "Path_of_the_chrome_driver"


driver = webdriver.Chrome(PATH)
driver.get("https://eduserve.karunya.edu/Login.aspx")
time.sleep(1)

# + FILL YOUR USER NAME AND PASSWORD  

driver.find_element(By.ID, "mainContent_Login1_UserName").send_keys("User_Name")
driver.find_element(By.ID, 'mainContent_Login1_Password').send_keys("Password")
driver.find_element(By.ID, 'mainContent_Login1_LoginButton').click()
time.sleep(1)
rows = (driver.find_element(By.XPATH, '//*[@id="ctl00_mainContent_grdHFB_ctl00"]/tbody/tr'))
if(driver.title == "Hourly Feedback"):
    try:
        for i in range(1,10):
            driver.find_element(By.XPATH,  f'/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[{i}]/td[5]/div/ul/li[4]').click()
    except:
        driver.find_element(By.ID, "mainContent_btnSave").click()
