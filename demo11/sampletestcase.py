
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_code():
  driver = webdriver.Chrome()
  # switch to frame
  driver.get('https://www.mercedes-benz.co.uk/passengercars')
  iframe = driver.find_element(By.CSS_SELECTOR, "#kx-proxy-tebu6a5nw")
  driver.switch_to.frame(iframe)

# capture shadow dom elements
  cssSelectorForHost1 = "dh-io-vmos[class='webcomponent aem-GridColumn aem-GridColumn--default--12']"
  shadowhost=driver.find_element(By.CSS_SELECTOR ,("dh-io-vmos[class='webcomponent aem-GridColumn aem-GridColumn--default--12'")).click()
  time.sleep(10)
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadowhost)
  print(shadowhost)
  shadow_root.find_element(By.CSS_SELECTOR("#hatchback-portaledId"))
 # shadow_root.find_element(By.CSS_SELECTOR("#hatchback-portaledId"))+
# shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadowhost")
  #shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
  #shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '#shadow_content')
  #assert shadow_content.text == 'contents'

# save screenshot of the webpage
  driver.save_screenshot("benz.png")

  driver.quit()
test_code()



