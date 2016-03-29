from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,os

browser = webdriver.Firefox() # Get local session of chrome
browser.maximize_window()
browser.get("http://test.xiaoshushidai.com") # Load page
elem = browser.find_element_by_id("fast_login").click()
user_input = browser.find_element_by_id("login-email-address").send_keys("hackred123")
user_pwd = browser.find_element_by_id("login-password").send_keys("a123456")
login_sub = browser.find_element_by_xpath("//*[@id='ajax-login-submit']").click()
meu = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]")
ActionChains(browser).move_to_element(meu).perform()
login_out = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[5]/a").click()
time.sleep(3)
browser.close()
'''
menu = browser.find_element_by_class_name('user_menu')
menu.click()
ActionChains(browser).move_to_element(login_out).perform()
#browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[5]/a").click()
tar = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[1]")
login_sub.click()
user_input.send_keys()
user_pwd = browser.find_element_by_id("login-password").send_keys("a123456")
user_pwd.send_keys("a123456")
user_input = browser.find_element_by_id("login-email-address")
login_sub = browser.find_element_by_id("ajax-login-submit").click()
login_out = browser.find_element_by_class_name('under_line_img')
login_out.click()
'''
'''
user_err = browser.find_element_by_class_name("dialog-content")
if(user_err==browser.find_element_by_class_name("dialog-content")){

}'''




