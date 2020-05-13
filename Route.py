import selenium
import time
from selenium import webdriver

chrome = webdriver.Chrome('/bin/chromedriver')


chrome.get('https://www.google.com/maps/d/u/0/edit?mid=18Lms1hvRbqIbNGzawuZ42z2kp3b56uWa&ll=12.789421073893198%2C78.87415999999996&z=9')
time.sleep(0.4)

login = chrome.find_element_by_xpath(r'//*[@id="identifierId"]')
login.send_keys('mur.kri.mad.rao')
nex = chrome.find_element_by_xpath(r'//*[@id="identifierNext"]/span')
nex.click()

time.sleep(0.4)
pas = chrome.find_element_by_xpath(r'//*[@id="password"]/div[1]/div/div[1]/input')
pas.send_keys('PbJqpalzm')
nex = chrome.find_element_by_xpath(r'//*[@id="passwordNext"]/span')
nex.click()






# Find the Know your Class & Section button and click it
dire = chrome.find_element_by_xpath(r'//*[@id="routeButton"]/div/div/div/div')
dire.click()

# Find the form in which you enter the SRN
From = chrome.find_element_by_xpath(r'//*[@id="input-waypoint-1-directions-layer-waypoint-item"]/div[2]/form/input')
From.send_keys('PES University, Outer Ring Road, Banashankari 3rd Stage, Banashankari, Bengaluru, Karnataka')
To = chrome.find_element_by_xpath(r'//*[@id="input-waypoint-2-directions-layer-waypoint-item"]')
To.send_keys('Elita Promenade, Phase 7, J. P. Nagar, Bengaluru, Karnataka')

ren = chrome.find_element_by_xpath(r'//*[@id="3wSJ34u4UI8-layer-header"]/div[3]')
ren.click()

rename = chrome.find_element_by_xpath(r'//*[@id=":51"]')
rename.click()

inp = chrome.find_element_by_xpath(r'//*[@id="update-layer-name"]/div[2]/input')

# Enter the current ID
inp.send_keys('Route')

save = chrome.find_element_by_xpath(r'//*[@id="update-layer-name"]/div[3]/button[1]')
save.click()