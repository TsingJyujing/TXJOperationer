# -*- coding: utf-8 -*-
from basic_libs import *
from configure import *
import string
import time


def selectcarLockState(terminal_id, car_id, cookiejar):
    rtn_str = urlOpen(
        api_selectcarLockState % (terminal_id, car_id),
        referer=txj_host + "system/login.do?documentHeight=756",
        cookie=generateCookiesString(cookiejar)
    )
    segs = rtn_str.split("#")
    if not len(segs) == 2:
        print "Undefined return, %s" % rtn_str
        return "", ""
    else:
        return segs[0].replace("<br/>", "\n"), string.atoi(segs[1])


def lockTaskIssued(carId, terminalId, lockType, cookiejar):
    result = string.atoi(urlOpen(
        api_lockTaskIssued_queryOnlineStatus % (carId, terminalId),
        referer=txj_host + "system/login.do?documentHeight=756",
        cookie=generateCookiesString(cookiejar)
    ))
    if result == 0:
        print "终端处于离线状态，无法下发操作!"
        return False
    elif result == 202:
        print "终端与发动机尚未建立连接，无法下发操作!"
        return False
    elif result == 1:
        if lockType in api_lockTaskIssued_oprs:
            result = string.atoi(urlOpen(
                api_lockTaskIssued_executeCommand % (carId, lockType),
                referer=txj_host + "system/login.do?documentHeight=756",
                cookie=generateCookiesString(cookiejar)
            ))
            return True
        else:
            print "操作符%s非法！" % lockType
            return False
    else:
        print "网站：我也不知道什么鬼原因反正没法操作！"
        return False


def lockTaskIssuedReason(carId, terminalId, lockType, cookiejar):
    result = string.atoi(urlOpen(
        api_lockTaskIssued_queryOnlineStatus % (carId, terminalId),
        referer=txj_host + "system/login.do?documentHeight=756",
        cookie=generateCookiesString(cookiejar)
    ))
    if result == 0:
        return "终端处于离线状态，无法下发操作!"
    elif result == 202:
        return "终端与发动机尚未建立连接，无法下发操作!"
    elif result == 1:
        if lockType in api_lockTaskIssued_oprs:
            result = string.atoi(urlOpen(
                api_lockTaskIssued_executeCommand % (carId, lockType),
                referer=txj_host + "system/login.do?documentHeight=756",
                cookie=generateCookiesString(cookiejar)
            ))
            return "操作%s %s 成功！" % (lockType, terminalId)
        else:
            return "操作符%s非法！" % lockType
    else:
        return "网站：我也不知道什么鬼原因反正没法操作！"



def loginWebsite(cookies_jar):
    try:
        rtn = urlOpen(
            url="http://www.sqtxj.com/system/login.do?documentHeight=756",
            referer="http://www.sqtxj.com/index.jsp",
            cookie=generateCookiesString(cookies_jar),
            postdata="userName=" + user_name + "&password=" + user_pwd + "&code="
        )
        return True
    except:
        return False
def main():
    cookies_jar, opener_rtn = installOpener()
    page_data = urlOpen(
        url="http://www.sqtxj.com/system/login.do?documentHeight=756",
        referer="http://www.sqtxj.com/index.jsp",
        cookie=generateCookiesString(cookies_jar),
        postdata="userName=" + user_name + "&password=" + user_pwd + "&code="
    )
    writeRaw("D:/txj_index.html", page_data)

    terminal_id = "1702281081"  # 1702241026
    car_id = "57034724"  # 57034723
    while True:
        print "车辆状态：\n%s\n状态代码：%d" % selectcarLockState(terminal_id, car_id, cookies_jar)
        time.sleep(2)


    while not lockTaskIssued(car_id, terminal_id, "close", cookies_jar):
        time.sleep(1)


if __name__ == "__main__":
    main()
