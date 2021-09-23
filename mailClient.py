#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time, pyperclip

def mailTo(login, password, email, text):
    pyperclip.copy(text)
    browser = webdriver.Firefox()
    browser.get('https://passport.yandex.com/auth?from=mail&origin=hostroot_homer_auth_com&retpath=https%3A%2F%2Fmail.yandex.com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1')
    loginBox = browser.find_element_by_id('passp-field-login')
    loginBox.send_keys(login)
    loginBox.submit()

    time.sleep(1.0)
    
    passwordBox = browser.find_element_by_id('passp-field-passwd')
    passwordBox.send_keys(password)
    passwordBox.submit()

    time.sleep(1.0)
    try:
        browser.find_element_by_class_name('passp-button').click()
        browser.find_element_by_class_name('mail-Wizard-Close').click()
    except:
        print()

    time.sleep(3.0)
    
    browser.find_element_by_class_name('mail-ComposeButton-Text').click()

    time.sleep(1.0)
    
    emailBox = browser.find_element_by_class_name('composeYabbles')
    emailBox.send_keys(email)

    time.sleep(1.0)
    htmlElem = browser.find_element_by_class_name('composeTextField')
 #   browser.find_element_by_css_selector('.cke_wysiwyg_div > div:nth-child(1)').click()
    pyperclip.paste()
    htmlElem.send_keys(text)
#    for i in range(10):
 #       time.sleep(1.0)
 #       htmlElem.send_keys(Keys.TAB)


    

if len(sys.argv) == 5:
    mailTo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print('Błędna ilość argumentów')
