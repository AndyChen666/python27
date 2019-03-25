#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2018/09/05
#淘宝秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time
 
def login():
    # 打开淘宝登录页，并进行扫码登彿
    browser.get("https://pc.xuexi.cn")
    time.sleep(3)
    if browser.find_element_by_id("C8putwnd60vk00"):
        browser.find_element_by_link_text("C8putwnd60vk00").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://www.xuexi.cn/")
    time.sleep(3)
''' 
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
 
def buy(times,choose):
    # 点击购物车里全选按钿
    if choose == 2:
        print("请手动勾选需要购买的商品")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结箿
        if now > times:
            if choose == 1:
                while True:
                    try:
                        if browser.find_element_by_id("J_SelectAll1"):                       
                            browser.find_element_by_id("J_SelectAll1").click()
                            break
                    except:
                        print("找不到全选按钿)
            try:
                if browser.find_element_by_id("J_Go"):
                    print("-----J_Go------")
                    print (browser.page_source)
                    browser.find_element_by_id("J_Go").click()
                    print("J_Go_end")
            except:
                print("-----pass------")
                pass
            while True:
                try:
                    print (browser.page_source)
                    if browser.find_element_by_link_text('提交订单'):
                        print('提交订单start')
                        browser.find_element_by_link_text('提交订单').click()
                        print('提交订单end')
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间＿s" % now1)
                except:
                    print("再次尝试提交订单")
            time.sleep(0.01)
 '''
if __name__ == "__main__":
    #times = input("请输入抢购时间，格式妿2018-09-06 11:20:00.000000):")
    #时间格式＿2018-09-06 11:20:00.000000"
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    #choose = input("到时间自动勾选购物车请输入‿”，否则输入‿”：")
    #buy(times,choose)
