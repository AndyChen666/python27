#-*- coding: UTF-8 -*-
import os
from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()
driver.maximize_window()
def login():
  driver.get("https://www.taobao.com")
  if driver.find_element_by_link_text("亲，请登录"):
    driver.find_element_by_link_text("亲，请登录").click();
  time.sleep(1)
  driver.get("https://cart.taobao.com/cart.htm")
  time.sleep(5)
  if driver.find_element_by_id("J_SelectAll1"):
    driver.find_element_by_id("J_SelectAll1").click()
  time.sleep(3)
  if driver.find_element_by_link_text("结 算"):
    driver.find_element_by_link_text("结 算").click();
  now = datetime.datetime.now()
  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
def buy_on_time(buytime):
  while True:
    now = datetime.datetime.now()
    if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
      while True:
        try:
          driver.find_element_by_link_text('提交订单').click()
        except:
          time.sleep(1)
    time.sleep(0.1)
#中文账号的时候要给它编码一下，不然会出错
login()
#login("英文账号",'密码')
buy_on_time('2019-03-12 19:41:00')
