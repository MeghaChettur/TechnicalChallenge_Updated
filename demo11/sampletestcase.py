import os

import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver import Remote, ActionChains
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select


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

  a = ActionChains(driver)
  shadow_root_3 = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/dh-io-vmos')
  outer_3 = expand_shadow_element(driver, shadow_root_3)
  buttons1 = outer_3.find_elements('css selector', 'div.dh-io-vmos_3dj27.dh-io-vmos_1_SKc.wb-new-colors > div > div > div > div > div > div:nth-child(4) > section > div:nth-child(1) > div.wb-grid-row.dh-io-vmos_tGY4l > div:nth-child(2) > div')
  for item in buttons1:
    text = item.text
    print(text)
    time.sleep(1)
  #Build = buttons1.find_element('css selector','#filters-placeholder').click()
  #WebElement  = driver.find_element('css selector', ('div.dh-io-vmos_3dj27.dh-io-vmos_1_SKc.wb-new-colors > div > div > div > div > div > div:nth-child(4) > section > div > div > div:nth-child(2) > div > wb-popover > ul > li:nth-child(2)'))
 # AclassSaloon = buttons1.find_element('css selector','div.dh-io-vmos_3dj27.dh-io-vmos_1_SKc.wb-new-colors > div > div > div > div > div > div:nth-child(4) > section > div > div > div:nth-child(2) > div > wb-popover > ul > li:nth-child(2) > a')

  driver.get('https://www.mercedes-benz.co.uk/passengercars/mercedes-benz-cars/car-configurator.html/motorization/CCci/GB/en/A-KLASSE/KOMPAKT-LIMOUSINE')
  shadow_root_4 = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/owcc-car-configurator')
  outer_4 = expand_shadow_element(driver, shadow_root_4)
  Button2 = outer_4.find_elements('css selector', '#cc-app-container-main > div.cc-app-container__main-frame.cc-grid-container > div.cc-grid-container.ng-star-inserted > div > div:nth-child(2) > cc-motorization > cc-motorization-filters > cc-motorization-filters-form > form > div')
  #Filter_Button = Button[1]
  #time.sleep(1)
  #Filter_Button.click()
  for items in Button2:
    text = items.text
    print(text)
    print(items.get_attribute('Fuel type'))
    option_Filter = select.select_by_index(2)
    print(option_Filter)
  ChooseFuel = items.get_attribute('Fuel type')
  #ChooseFuel.click()
  time.sleep(1)

  driver.save_screenshot("benz.png")

  driver.quit()




 # Fueltype = Filter.find_element('css selector','#cc-app-container-main > div.cc-app-container__main-frame.cc-grid-container > div.cc-grid-container.ng-star-inserted > div > div:nth-child(2) > cc-motorization > cc-motorization-filters > cc-motorization-filters-form > form > div > div.cc-motorization-filters-form__primary > div.cc-motorization-filters-form__primary-filters.ng-star-inserted > cc-motorization-filters-primary-filters > div > fieldset > wb-multi-select-control')
 # Filter_Diesel = Select(driver.find_element('css selector','//*[@id="cc-app-container-main"]/div[2]/div[2]/div/div[2]/cc-motorization/cc-motorization-filters/cc-motorization-filters-form/form/div/div[1]/div[2]/cc-motorization-filters-primary-filters/div/fieldset/wb-multi-select-control/button'))


  #os.system('pause')


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



