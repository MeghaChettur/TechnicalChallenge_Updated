import os

import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver import Remote
def start_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('--start-maximized')
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(options=options)
  return driver
  # switch to frame

def expand_shadow_element(driver, element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

def accept_cookies(driver):
  shadow_root_1 = driver.find_element('xpath', '/html/body/cmm-cookie-banner')
  outer = expand_shadow_element(driver, shadow_root_1)
  time.sleep(5)
  button = outer.find_element('css selector', 'div > div > button.wb-button.wb-button--primary.wb-button--small.wb-button--accept-all')
  button.click()


def main():
  driver = start_driver()
  driver.get('https://www.mercedes-benz.co.uk/passengercars')
  accept_cookies(driver)
  time.sleep(1)
  return driver



if __name__ == '__main__':
  driver = main()



  #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
  #time.sleep(2)
  shadow_root_2 = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/dh-io-vmos')
  outer_2 = expand_shadow_element(driver, shadow_root_2)
  buttons = outer_2.find_elements('css selector', '.dh-io-vmos_1RKkS')
  hatchback_button = buttons[3]
  hatchback_button.click()
  time.sleep(1)
  hatchback_button.click()
  #hatchback_button = outer_2.find_element('css selector', '#filters-placeholder > div > div > section:nth-child(2) > button:nth-child(5)')
  #print(hatchback_button)
  #hatchback_button.click()
  #cookie_accept_button = outer.find_element('xpath', '/div/div/div[2]/cmm-buttons-wrapper/div/div')
  #cookie_accept_button.click()
  #print(cookie_accept_button)
  #hatchbacks_button_xpath = '/html/body/div[1]/div/div[1]/div/dh-io-vmos//div[2]/div[3]/div/div/div[1]/div/div/section[2]/button[4]'
  #driver.find_element('xpath', hatchbacks_button_xpath)
  os.system('pause')


  #iframe = driver.find_element(By.CSS_SELECTOR, "#kx-proxy-tebu6a5nw")
  #driver.switch_to.frame(iframe)

# capture shadow dom elements
  #string = "dh-io-vmos[class='webcomponent aem-GridColumn aem-GridColumn--default--12']"
  #shadowhost=driver.find_element(By.CSS_SELECTOR ,("dh-io-vmos[class='webcomponent aem-GridColumn aem-GridColumn--default--12'"))
 # shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadowhost)
  #print(driver.page_source)
  #print(shadow_root)
  #shadowcontent = driver.find_element(By.CSS_SELECTOR("webcomponent webcomponent-nested wb-grid-col-mq6-3 wb-grid-col-mq4-4 wb-grid-col-mq3-6 wb-grid-col-mq1-12 owc-wb-grid-col-mq-2-3-midpoint owc-simple-teaser-item wb-content-slider__item wb-card wb-card--white aem-GridColumn aem-GridColumn--default--12"))

  #time.sleep(1000)
  #driver.save_screenshot("benz.png")
  #print(shadow)
  #shadow.find_element(By.CSS_SELECTOR("#hatchback-portaledId"))
  #shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadowhost)

  #print(type(shadow_root))
  #shadow_content= shadow_root.find_element(By.CSS_SELECTOR('dh-io-vmos[class='webcomponent aem-GridColumn aem-GridColumn--default--12']'))
  #print(shadow_content)

 # shadow_root.find_element(By.CSS_SELECTOR("#hatchback-portaledId"))+
# shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadowhost")
  #shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
  #shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '#shadow_content')
  #assert shadow_content.text == 'contents'

# save screenshot of the webpage



  #driver.quit()

#test_code()



