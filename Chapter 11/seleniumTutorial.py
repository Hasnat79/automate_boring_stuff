from selenium import webdriver

browser = webdriver.Firefox()
# print(type(browser))
# browser.get('http://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('card-img-top')
#     print('Found <%s> element with that class name!'%(elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

# linkElem=browser.find_element_by_link_text('Read Online for Free')
# print(type(license))
# linkElem.click()

browser.get('https://mail.google.com')
emailElem=browser.find_element_by_id('identifierId')
emailElem.send_keys('gmail ID gmail.com')
btnElem=browser.find_element_by_class_name("CwaK9")
btnElem.click()
browser.implicitly_wait(5)

passElem=browser.find_element_by_xpath(".//*[@id='password']//input[@name='password']")
passElem.send_keys("pass")
# RveJvd snByac