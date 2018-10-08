import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('http://www.comicsexperience.com/scripts/')
#assert 'Google' in browser.title

#elem = browser.find_element_by_name('q')
#elem.send_keys('nathan' + Keys.RETURN)
#time.sleep(5)

#browser.quit()

pdf = browser.find_element_by_partial_link_text("(PDF)")
print(pdf)
print("\n" + type(pdf))
browser.quit()