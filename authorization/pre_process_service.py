# purpose:
# remove services that don't nedd auth
# link service with their passwd

import sys
from builtins import  KeyError, property
from cmath import pi
from lib2to3.pgen2 import token
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
from tools import *



def clear_already_connect_services():
    browser.get("https://ifttt.com/my_services")
    web_eles = browser.find_elements_by_css_selector(".service-item [href]")
    links = [elem.get_attribute('href') for elem in web_eles]
    print(links)

    for link in links:
        browser.get(link + "/settings")
        
        #found = check_exists_by_css_selector(browser, ".top [href]")
        
            # settings_url = browser.find_element_by_css_selector(".top [href]").get_attribute('href')
            # browser.get(settings_url)
        browser.find_element_by_class_name("remove").click()
        alert = browser.switch_to.alert
        alert.accept()
        



# parse parameter
start_line = int(sys.argv[1])
end_line = int(sys.argv[2])
print(start_line, end_line)

## load services url info
f = open("services_home_url.txt", "r")
lines = f.readlines()[start_line: end_line]
##


# connect to ifttt
browser = webdriver.Chrome('/Users/liuhuo/Documents/chromedriver')
browser.get('https://ifttt.com/login?wp_=1')

username = browser.find_element_by_id("user_username")
password = browser.find_element_by_id("user_password")

username.send_keys("user_email@example.com")
password.send_keys("password")

browser.find_element_by_name("commit").click()

# clear_already_connect_services()


to_be_connect_files = "service.txt"
no_connection_files = "no_connection.txt"

f1 = open(to_be_connect_files, "a")
f2 = open(no_connection_files, "a")
# check url 




for line in lines:
    tokens = line.split(",")
    if len(tokens) < 3:
        continue

    to_be_connect = tokens[len(tokens)-1].replace(" ", "").replace("\n", "")
    print(to_be_connect)

    browser.get(to_be_connect)
    found  = check_exists_by_link_text(browser,"Connect")
    if found:
        f1.write(line)
    else:
        f2.write(line)



