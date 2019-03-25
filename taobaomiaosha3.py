#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains
  

file_object1 = open("F:/GitHub/python27/test1file.txt", 'w')
file_object2 = open("F:/GitHub/python27/test2file.txt", 'w')

  
  
driver = webdriver.Chrome()
driver.maximize_window()
  
  
def login():
 # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在30秒内完成扫码")
        time.sleep(10)
        driver.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)
 # 点击购物车里全选按钮
 # if driver.find_element_by_id("J_CheckBox_939775250537"):
 # driver.find_element_by_id("J_CheckBox_939775250537").click()
 # if driver.find_element_by_id("J_CheckBox_939558169627"):
 # driver.find_element_by_id("J_CheckBox_939558169627").click()
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
  
def buy(buytime):
    #while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
 # 对比时间，时间到的话就点击结算
        if True:#now > buytime:
            print("-----!!!------")
            try:
  # 点击结算按钮
                
                source1=driver.page_source
                print(source1,file = file_object1)
                #str(source1)
                #file_object1.writelines(source1)
                print("----------------")
                file_object1.close( )
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    sleep(1)
                    #windows = driver.current_window_handle
                    #driver.switch_to.window(windows)
                    print("------------------------")
                    source=driver.page_source
                    print(source,file = file_object2)
                    #str(source)
                    #file_object2.writelines(source)
                    file_object2.close( )
                    print("------------------------")
                    
                    if driver.find_element_by_link_text("提交订单"):
                        driver.find_element_by_link_text("提交订单").click()
                        print("111115")
            except:
                time.sleep(0.1)
            print(now)
            time.sleep(0.1)
  
  
if __name__ == "__main__":
 # times = input("请输入抢购时间：")
 # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2019-03-12 23:26:00.000000")

 
