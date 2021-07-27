#! Python 3
# T.M 22/07/21

import re, sys
from selenium import webdriver

#Step 1: Take IP from user, store in variable
ip=input('Enter IP Here: ', )

#Step 2: Compare IP with regex statement ensuring it is correct
try:
    if re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(ip)):
        print('That is a valid IP!\nSearching please wait...')
    else:
        thread.exit()
except:
    print('An errror has occured, please ensure you entered a valid IP and try again.')
    sys.exit()

#Step 3: Open Firefox Browser
browser=webdriver.Firefox()
browser.implicitly_wait(5) #Wait for browser to load to prevent race condition error
main_window = browser.current_window_handle

#Step 4: Search IP on Virus Total
browser.get('https://www.virustotal.com/gui/ip-address/'+ip)

#Step 5: Search IP on IP Void on a New Tab
browser.execute_script("window.open('https://www.ipvoid.com/ip-blacklist-check/')")
browser.switch_to_window(browser.window_handles[1])
searchElem2=browser.find_element_by_id('ipAddr')
searchElem2.clear()
searchElem2.send_keys(str(ip))
searchElem2.submit()

#Step 7: Search IP on Mx Toolbox on a New Tab
browser.execute_script("window.open('https://mxtoolbox.com/blacklists.aspx');")
browser.switch_to_window(browser.window_handles[2])
searchElem3a=browser.find_element_by_id('ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput')
searchElem3a.clear()
searchElem3a.send_keys(str(ip))
searchElem3b=browser.find_element_by_id('ctl00_ContentPlaceHolder1_ucToolhandler_btnAction')
searchElem3b.click()

#Step 8: Search IP on IBM X-Force on a New Tab
browser.execute_script("window.open('https://exchange.xforce.ibmcloud.com/');")
browser.switch_to_window(browser.window_handles[3])
browser.implicitly_wait(2)
## Click the checkbox and enter a guest login
searchElem4a=browser.find_element_by_id('termsCheckbox')
searchElem4a.click()
searchElem4b=browser.find_element_by_css_selector('.guestlogin > a:nth-child(1)')
searchElem4b.click()
browser.implicitly_wait(2)
## Search for the IP
searchElem4c=browser.find_element_by_id('top_search')
searchElem4c.clear()
searchElem4c.send_keys(str(ip))
searchElem4c.submit()

#Step 9: Exit Program
print('Please see Firefox for the results, goodbye :)')
sys.exit()