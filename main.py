from selenium import webdriver
import time
import sys
driver = webdriver.Chrome()
driver.get("https://www.surveycake.com/s/2xOyK")
time.sleep(3)

#現金
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/span/span[2]")
button.click()

#實領 6,000元或以上
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[7]/div/span/span[2]")
button.click()

#新北市
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/span/span[2]")
button.click()

#40-49歲
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[4]/div/span/span[2]")
button.click()

#男性
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/div[2]/div[2]/div/div[1]/div/span/span[2]")
button.click()

#送出
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[1]/div/div[2]/button/span")
button.click()

#確定送出
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
button = driver.find_element_by_xpath("/html/body/div[2]/div/footer/button[2]/span")
button.click()

time.sleep(2)
# driver.close()
driver.quit()