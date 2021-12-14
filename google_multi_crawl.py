from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
          os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")


searchList = ['오징어게임', '오일남']

for search in searchList:
  time.sleep(1)
  elem = driver.find_element_by_name("q")
  elem.clear()
  time.sleep(1)
  elem.send_keys(search)
  time.sleep(1)
  elem.send_keys(Keys.RETURN)
  time.sleep(1)

  SCROLL_PAUSE_TIME = 1
  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      try:
        driver.find_element_by_css_selector(".mye4qd").click()
      except:
        break
    last_height = new_height

  images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
  count = 1
  createFolder("multiCrawling" + "/" + search)
  for image in images:
    try:
      image.click()
      time.sleep(1)
      imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
      opener=urllib.request.build_opener()
      opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
      urllib.request.install_opener(opener)
      urllib.request.urlretrieve(imgUrl, "multiCrawling/" + search + "/" +  str(count) + ".jpg")
      count = count + 1
    except:
      pass

driver.close()


