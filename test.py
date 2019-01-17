from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path = "D:\\geckodriver")
driver.get("http://www.sougou.com")
driver.find_element_by_id("query").clear()
driver.find_element_by_id.send_keys(u"baidu")
driver.find_element_by_id("stb").click()
time.sleep(3)
driver.quit()
