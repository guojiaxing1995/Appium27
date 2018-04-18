#coding=utf-8
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.get_by_local import GetByLocal

capabilities = {
  "platformName": "Android",
  "deviceName": "K4Q6T16713001686",
  "automationName": "uiautomator2",
  "app": r"D:\PycharmProjects\Appium27\apk\wdfp.apk",
  #"noReset":"True"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)

#driver.swipe()
def get_size():
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']

    return width,height

def slide_up():
    width,height = get_size()
    driver.swipe(width/2,height/10*9,width/2,height/10*1,2000)

def slide_left():
    width,height = get_size()
    driver.swipe(width/10*9,height/2,width/10,height/2,1000)

def get_tost():
    tost_element = ("xpath","//*[contains(@text,'手机号不能为空')]")
    WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_element_located(tost_element))


sleep(2)
slide_up()
sleep(1)
slide_left()
sleep(1)
slide_left()
sleep(1)
slide_left()
sleep(1)
slide_left()
sleep(5)
# getByLocal = GetByLocal(driver)
# getByLocal.get_element('login_element','carouselfigure').click()
# #driver.find_element_by_class_name('android.widget.ImageView').click()
# getByLocal.get_element('login_element','username').send_keys('18550903915')
# #driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('18550903915')
# driver.hide_keyboard()
# driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys('qwe123')
# driver.hide_keyboard()
# getByLocal.get_element('login_element','loginbutton').click()
# #driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
# #get_tost()
# sleep(5)
# driver.find_element_by_android_uiautomator('new UiSelector().text("服务")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
# sleep(5)
element = driver.find_element_by_android_uiautomator('new UiSelector().text("发现")')
driver.find_elements_by_xpath()
n = element.size


#webview = driver.contexts
#print(webview)

#S7TDU15424008121
#K4Q6T16713001686
#DU2TAN149P079327

