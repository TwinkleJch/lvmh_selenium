from selenium import webdriver
import random
from time import sleep
import ddddocr
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#打开浏览器
def open():
    # driver.maximize_window()
    driver.get('https://www.louisvuitton.cn/zhs-cn/homepage?utm_source=baidu&utm_medium=cpc&utm_campaign=A1_X_OT_E_BZ_BZ_D_E_AO_RTOMNI&utm_term=LG-H1')
    # print(driver.get_cookies())
    # now_handle = driver.current_window_handle
    # driver.switch_to.window(now_handle)
    sleep(2)

#同意cookie
def agree():
    driver.delete_all_cookies()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/ul/li[3]/button').click()
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/a').click()
    driver.delete_all_cookies()
    sleep(1)

#搜索
def search():
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/header/div/div/nav[2]/ul/li[1]/div/button').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/header/div/form/div/input').send_keys('1AAGXD')
    sleep(1)
    # driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/header/div/form/div/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/header/div[2]/div/div[2]/div/div/div/a').click()
    sleep(2)

while 1:
    open()
    agree()
    search()
    try:
        color = driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[3]/button[1]/span[2]').text#颜色
        inch=driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[3]/button[2]/span[2]').text#尺码
        print('初始色码：',color,inch)
        break
    except:
        print('出错了')
        driver.close()
        driver = webdriver.Chrome()

if color != '黑色':
    driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[3]/button[1]').click()#颜色的箭头
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div/ul/li[2]/div').click()#对应颜色
    sleep(2)
if inch != '08.0':
    driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[3]/button[2]').click()#尺码的箭头
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div/ul/li[8]').click()#对应尺码
    sleep(2)
color = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[3]/button[1]/span[2]').text  # 颜色
inch = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[3]/button[2]/span[2]').text  # 尺码
print('现在色码：',color, inch)
buttun=driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/div[1]/section/div[2]/div/div/div[5]').text#按钮
print(buttun)
