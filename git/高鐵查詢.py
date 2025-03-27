from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

#開啟網頁，點擊同意cookie
driver.get('https://irs.thsrc.com.tw/IMINT/')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.policy-btn-accept').click()
#選擇出發站
start = '南港'
driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[4]/div[1]/div/div[1]/div/select').send_keys(start)
#選擇抵達站
destination = '左營'
driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[4]/div[1]/div/div[2]/div/select').send_keys(destination)

#選擇出發日期(手動)
#dd = '2024/02/29'
driver.find_element(By.CSS_SELECTOR,'.uk-child-width-1-2 > div:nth-child(1) > div:nth-child(1)').click()
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR,'.uk-child-width-1-2 > div:nth-child(1) > div:nth-child(1)').send_keys(dd)

#選擇出發時間
tt = '08:00'
driver.find_element(By.NAME,'toTimeTable').send_keys(tt)

#車票數量
p = '2'
driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[5]/div/div[1]/div/select').send_keys(p)

#車次需求
driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[6]/div[1]/div/div').click()
type = '3' #選擇1,2,3=>依序為所有車次,限定早鳥優惠車次,無需早鳥(全票以原價計)
if type == '1':
    driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[6]/div[1]/div/div/select/option[1]').click()
elif type == '2':
    driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[6]/div[1]/div/div/select/option[2]').click()
else:
    driver.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[6]/div[1]/div/div/select/option[3]').click()

#手動輸入驗證碼
time.sleep(5)
#提交表單
driver.find_element(By.NAME,'SubmitButton').click()
