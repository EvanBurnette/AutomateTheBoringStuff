import os, sys, time, json, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def validateEmail(email):
    emailRe = re.compile(r'''([a-zA-Z0-9.])+
                         (@)
                         ([a-zA-Z0-9])+
                         (\.)
                         (com|edu|org|co\.uk|.net|.gov)''', re.VERBOSE)
    if emailRe.search(email) != None:
        return True
    else:
        return False

if validateEmail(sys.argv[1]):
    print('Recipient email is valid')
    print('Opening gmail')
else:
    print('Recipient email should be first argument after program name')
    print('python cmdEmail.py <EmailOfRecipient@site.com> "Subject of message" "Message in quotes"')
    print('Make sure address is free from errors')
    quit()

toEmail = sys.argv[1]

os.chdir(r'''C:\Users\EvanB\Documents\MyPrograms\AutomateTheBoringStuff''')

with open('junkEmailGate.json', encoding='utf-8') as fileHandle:
    userData = json.load(fileHandle)

browser = webdriver.Firefox()

browser.get('http://gmail.com')
time.sleep(1)
emailAddress = browser.find_element_by_id('identifierId')
time.sleep(1)
emailAddress.send_keys(userData['emailAddress'])
emailAddress.send_keys(Keys.ENTER)
time.sleep(1)

password = browser.find_element_by_name('password')
password.click()
password.send_keys(userData['gateCode'])
password.send_keys(Keys.ENTER)
time.sleep(2)

body = browser.find_element_by_tag_name('body')
body.send_keys('c') # Toggle <settings/general/Keyboard shortcuts on> in gmail
time.sleep(2)
toEmailField = browser.find_element_by_name('to')
toEmailField.send_keys(toEmail)

subjectField = browser.find_element_by_name('subjectbox')
subjectField.send_keys(sys.argv[2])

messageBody = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
messageBody.send_keys(sys.argv[3])
time.sleep(1)

body = browser.find_element_by_tag_name('body')
ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
time.sleep(1)

userButton = browser.find_element_by_class_name("gbii")
userButton.click()
signOut = browser.find_element_by_id("gb_71")
signOut.click()

browser.close()
