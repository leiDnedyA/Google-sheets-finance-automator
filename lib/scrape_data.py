import json

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium setup
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(options=options)

# loads secret.json
f = open('secret.json')
secretJSON = json.load(f)

# scrapes dining points balance from website
def getBeaconCardBalance():

    # log into microsoft account
    browser.get("https://beaconcard.umb.edu/login.php")
    EMAILFIELD = (By.ID, 'i0116')
    PASSWORDFIELD = (By.ID, 'i0118')
    NEXTBUTTON = (By.ID, 'idSIButton9')
    TWOFACTORBUTTON = (By.CSS_SELECTOR, 'div .table')
    MOBILEVERIFICATIONFIELD = (By.ID, 'idTxtBx_SAOTCC_OTC')
    VERIFYTWOFACTORBUTTON = (By.ID, 'idSubmit_SAOTCC_Continue')

    umb_password = secretJSON['umb_password']

    # TODO: disable or change two factor authentication on microsoft account

    # wait for email field and enter email
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("ayden.diel001@umb.edu")
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(umb_password)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(TWOFACTORBUTTON)).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(MOBILEVERIFICATIONFIELD)).send_keys(input('2 Factor Text Code: '))
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(VERIFYTWOFACTORBUTTON)).click()
    
    

getBeaconCardBalance()

# scrapes bank ccount balance from Citizens website
def getBankAccountBalance():
    pass
    # 