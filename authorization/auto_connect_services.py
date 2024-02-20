####################self defined tools######################
from distutils import text_file
from gettext import find
from math import fabs
from tools import *
############################################################
from builtins import  KeyError, property
from cmath import pi
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from pymongo import MongoClient
from selenium.webdriver.common.action_chains import ActionChains


name_kw = ["username", "auth-username", "inputEmail","name-username","Email","inputEmail","emailLogin","email", "e-mail", "user", "User" ,"Username", "User Name","user_id", "Userid", "UserID", "UserId", "id", "ID", "Id", "identifierId"]
passwd_kw = ["passwd","name-password" ,"inputPassword", "auth-password","password", "Password", "inputPassword", "User Password", "passwordLogin"]
button_xpath_kw = ["_submit", "submit", "Submit", "Sign in", "Sign In", "login","LogIn", "log", "log in", "Log In","login_button","signIn", "identifierNext", "passwordNext"]
button_class_kw = ["btn-primary", "cta-btn disabled", "loginButtons"]



user_input = "***" ## user email address 
passwd_input = "***"


def getActivationList():
    href_list = []
    browser.get('https://ifttt.com/channels/activation_list?is_web_view=1')
    applet_page_response = browser.page_source
    applet_page_content = BeautifulSoup(applet_page_response, "html.parser")
    list_div = applet_page_content.find('div', {'id': 'channel_activation_list'})
    a_list = list_div.findChildren("a", recursive=True)
    for a in a_list:
        href_list.append(a['href'])

    return href_list


def find_kw_by_differnt_method(kw):
    Found = check_exists_by_id(browser,kw)
    if Found:
        print("Found by id: " + kw )
        web_ele =  browser.find_element_by_id(kw)
        return web_ele

    Found = check_exists_by_name(browser, kw)
    if Found:
        print("Found by name: " + kw )
        web_ele =  browser.find_element_by_name(kw)
        return web_ele
    

    xpath_list = possible_xpath(kw)
    for xpath in xpath_list:
        Found = check_exists_by_path(browser, xpath)
        if Found:
            web_ele = browser.find_element_by_xpath(xpath)
            print("Found by xpath: " + xpath)
            return web_ele



    css_selector = "." + kw
    Found = check_exists_by_css_selector(browser, css_selector)
    if Found:
        web_ele = browser.find_element_by_css_selector(css_selector)
        print("Found by css selector: " + css_selector)


    Found = check_exists_by_class_name(browser, kw)
    if Found:
        web_ele = browser.find_element_by_class_name(kw)
        print("Found by class name: " + kw)
        return web_ele
    return None



def find_ele_by_kw(browser, kw_array):
    found = False
    # web_ele = selenium.webdriver.remote.webelement.WebElement()
    for kw in kw_array:
            web_ele = find_kw_by_differnt_method(kw)
            if web_ele != None:
                found = True
                return web_ele, found
    return None, found

def login_with_uid_pwd(browser, origin_url):
    print("try login_with_uid_pwd")
    uid, u_found = find_ele_by_kw(browser, name_kw)
    pid, p_found = find_ele_by_kw(browser, passwd_kw)
    sign_id, s_found = find_ele_by_kw(browser, button_xpath_kw)
    if s_found == False:
        sign_id, s_found = find_ele_by_kw(browser, button_class_kw)

    if u_found and p_found and s_found:
        try:
            uid.send_keys(user_input)
        except ElementNotInteractableException:
            return False
            # browser.implicitly_wait(2)
            # ActionChains(browser).move_to_element(uid).send_keys(user_input).perform()

        try:
            pid.send_keys(passwd_input)
        except ElementNotInteractableException:
            return False
            # browser.implicitly_wait(2)
            # ActionChains(browser).move_to_element(pid).send_keys(passwd_input).perform()

        try:
            sign_id.click()
        except ElementNotInteractableException:
            perform_action_click(browser, sign_id)
        return True
    return False

def login_two_steps_1(browser, origin_url): # first step sign in second step uid pid sign
    print("try login_two_steps_1")
    sign_btn, btn_found = find_ele_by_kw(browser, button_xpath_kw)
    if btn_found:
        sign_btn.click()
        time.sleep(10) # wait next page to load
        if browser.current_url != origin_url:
            return login_with_uid_pwd(browser, browser.current_url)
    return False

def login_amazon(browser, origin_url):  # first authorize amazon, then login in
    print("try login_amazon")
    css_selector = '[alt="Login with Amazon"]'
    found = check_exists_by_css_selector(browser,css_selector)
    if found:
        sign_btn = browser.find_element_by_css_selector('[alt="Login with Amazon"]')
        sign_btn.click()
        time.sleep(10) # wait next page to load
        if browser.current_url != origin_url:
            return login_with_uid_pwd(browser, browser.current_url)
    return False


# def login_google(origin_url): # if google provide gmail account

def login_two_steps_2(browser, origin_url):# first step enter email, second step pass sign
    print("try login_two_steps_2")
    uid, u_found = find_ele_by_kw(browser, name_kw)
    btn_next, next_found = find_ele_by_kw(browser, button_xpath_kw)

    if u_found and next_found:
        uid.send_keys(user_input)
        btn_next.click()
        
        time.sleep(6)
        if browser.current_url == origin_url: # clcik failed
            return False

        pwd, p_found = find_ele_by_kw(browser, passwd_kw)
        btn_confirm, confirm_found = find_ele_by_kw(browser, button_xpath_kw)
        if p_found and confirm_found:
            pwd.send_keys(passwd_input)
            btn_confirm.click()

            time.sleep(10)
            if browser.current_url != origin_url:
                return True 
    return False


def perform_action_click(webdriver, element):
    action = ActionChains(webdriver)
    action.click(on_element=element)
    action.perform


def connect_username_passwd(url, phase1_file, phase2_file):
    browser.get(url)
    global passwd_input
    passwd_input = get_special_pwd(url)
    mark_url = url


    url = browser.current_url
    time.sleep(5) # wait page to load
    text_info_before_auth = get_visible_text_from_page(browser)
    phase1_file.write(text_info_before_auth)

    print("ready")
    ###### step1 login using uid pwd and sign in button
    success1, success2, success3, success4 = False, False, False, False

    # ###### step2 login in first then step1
    # ###### step3 type email btn first, then passwd btn 
    success1 = login_with_uid_pwd(browser, url)
    if success1 == False:
        print("auth failed: " , mark_url)
    # if success1 == False:
    #     success2 = login_two_steps_1(browser, url)
    # if success1 == False and success2 == False:
    #     success3 = login_amazon(browser,url)
    # # if success1 == False and success2 ==  False and success3 == False:
    # #     #success4 = login_two_steps_2(browser, url)
    # #     return
    
    # if success1 or success2 or success3:
    #     print("auth successfully: ", mark_url)
    # else:
    #     print("auth failed: ", mark_url)    

    time.sleep(50)
    text_info_after_auth = get_visible_text_from_page(browser)
    phase2_file.write(text_info_after_auth)
    return

#################################### begin to login to ifttt ###################################

browser = webdriver.Chrome('/Users/liuhuo/Documents/chromedriver')
browser.get('https://ifttt.com/login?wp_=1')

username = browser.find_element_by_id("user_username")
password = browser.find_element_by_id("user_password")



username.send_keys("user_email@example.com")
password.send_keys("password")

browser.find_element_by_name("commit").click()
# href_list = getActivationList()

#start line exclude, end line include
start =  int(300)
end =  int(727)
href_f = open("href_list.txt", "r")
href_list = href_f.readlines()[start:end]


dir_name = "auth_log"



###################### for some manually work
# href_list = [
#   
# ]

# print(href_list)
#######################


for to_be_connect_service in href_list:
    to_be_connect_service = to_be_connect_service.replace("\n", "")
    url = "https://ifttt.com" + to_be_connect_service
    if check_vaild_connection_url(url) == False:
        continue

    if check_browser_url(browser,url) == False:
        continue
    
    print("#########################################################")
    print("begin to connect to service: " + url)

    # create file for text info before and after auth
    text_name = dir_name + "/" + to_be_connect_service.replace("/", "_").replace("activate?is_web_view=1", "")
    print(text_name)

    text_file_phase1 = open(text_name + "_phase1", "w+")
    text_file_phase2 = open(text_name + "_phase2", "w+")

    connect_username_passwd(url, text_file_phase1, text_file_phase2)
    print("###########################################################")
