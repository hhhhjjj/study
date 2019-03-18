# coding=utf-8
from splinter.browser import Browser
from time import sleep
import traceback
user_name = input("账号")
password = input("密码")
# 账号密码
d_time = u"2019-02-04"
# 时间
starts = u"%u4E0A%u6D77%2CSHH"
# 始发站cookie，这里是上海的
ends = u"%u6606%u660E%2CKMM"
# 终点站cookie
order = 1
# 页面上第几趟火车
ticket_url = u"https://kyfw.12306.cn/otn/leftTicket/init"
login_url = u"https://kyfw.12306.cn/otn/login/init"
initmy_url = u"https://kyfw.12306.cn/otn/view/index.html"


def login():
    b.find_by_text(u"登录").click()
    sleep(3)
    b.find_by_text(u"账号登录").click()
    sleep(0.5)
    b.find_by_id(u"J-userName").fill(user_name)
    sleep(1)
    b.find_by_id(u"J-password").fill(password)
    sleep(1)
    print(u"自己手动选择验证码图片并且点击登录")
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break


def huo_che():
    global b
    b = Browser(driver_name="chrome")
    # 选择其他的浏览器需要换其他的webdriver，webdriver需要设置在环境变量
    b.visit(ticket_url)
    while b.is_text_present(u"登录"):
        sleep(1)
        login()
        if b.url == initmy_url:
            break
    try:
        print(u"购票页面...")
        # 跳回购票页面
        b.visit(ticket_url)
        # 加载查询信息
        b.cookies.add({u"_jc_save_fromStation": starts})
        b.cookies.add({u"_jc_save_toStation": ends})
        b.cookies.add({u"_jc_save_fromDate": d_time})
        b.reload()
        sleep(2)
        count = 0
        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print(u"循环点击查询... 第 %s 次" % count)
                sleep(1)
                # 时间间隔可调，但是12306有反爬系统
                try:
                    b.find_by_text(u"预订")[order-1].click()
                    break
                except Exception as e:
                    print(e)
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print(u"循环点击查询... 第 %s 次" % count)
                sleep(1)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except Exception as e:
                    print(e)
                    continue
        b.find_by_id(u"normalPassenger_0").click()
        # 这个是选择常用联系人，0代表选的常用联系人列表的第一个乘客
        b.find_by_id(u"submitOrder_id").click()
        sleep(0.5)
        b.find_by_id(u"qr_submit_id").click()
        print(u"自行支付")
    except Exception as e:
        print(e)
        print(traceback.print_exc())


if __name__ == "__main__":
    huo_che()
