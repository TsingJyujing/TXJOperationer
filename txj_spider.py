# -*- coding: utf-8 -*-
from basic_libs import *
from configure import *
import string
import re


def selectcarLockState(terminal_id, car_id, cookiejar):
    sdict = {-2:"不具备锁车功能",-1:"未激活锁车功能",0:"未锁车",1:"已锁车",2:"正在锁车中",3:"正在解锁中",4:"未锁车，锁车失败",5:"未解锁，解锁失败",12:"未激活，激活失败！",15:"未解锁，解锁失败！"}
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
        if sdict.has_key( string.atoi(segs[1]) ):
            reason = sdict[string.atoi(segs[1])]
        else:
            reason = "尚不能解析的代码"
        return segs[0].replace("<br/>", "\n"), string.atoi(segs[1]), reason


def getCarID(terminal_id, cookiejar):
    try:
        doc = urlOpen(
            api_loadCarInfo % terminal_id,
            referer=txj_host + "system/login.do?documentHeight=756",
            cookie=generateCookiesString(cookiejar)
        )
        reexp = r'onclick=\"manageTerminalIdList.*?</a>'
        find_res = re.findall(reexp, doc)
        if  len(find_res) == 0:
            return "找不到你要的CarID，请检查输入是否正确"
        info = []
        for res in find_res:
            terminal_id = re.findall(r">\d*?<", res)[0][1:-1]
            carid = re.findall(r"'\d*?'", res)[0][1:-1]
            info.append("终端号:%s，CARID:%s" % (terminal_id, carid))
        return "查询结果：\n" + "\n".join(info)
    except:
        return "找不到你要的CarID，请检查输入是否正确"


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
            result = urlOpen(
                api_lockTaskIssued_executeCommand % (carId, lockType),
                referer=txj_host + "system/login.do?documentHeight=756",
                cookie=generateCookiesString(cookiejar)
            )
            return "操作%s %s 成功！" % (lockType, terminalId)
        else:
            return "操作符%s非法！" % lockType
    else:
        return "网站：我也不知道什么鬼原因反正没法操作！"



def loginWebsite(cookies_jar):
    try:
        rtn = urlOpen(
            url=txj_host + "system/login.do?documentHeight=756",
            referer=txj_host + "index.jsp",
            cookie=generateCookiesString(cookies_jar),
            postdata="userName=" + user_name + "&password=" + user_pwd + "&code="
        )
        return True
    except:
        return False


def main():
    cookies_jar, opener_rtn = installOpener()
    page_data = urlOpen(
        url=txj_host + "system/login.do?documentHeight=756",
        referer=txj_host + "index.jsp",
        cookie=generateCookiesString(cookies_jar),
        postdata="userName=" + user_name + "&password=" + user_pwd + "&code="
    )
    writeRaw("D:/txj_index.html", page_data)

    terminal_id = "1702241026"
    car_id = "57034723"  # 57034723
    print getCarID(terminal_id, cookies_jar)
    print getCarID("17", cookies_jar)
    print getCarID("99999", cookies_jar)
    #lockTaskIssuedReason(car_id, terminal_id, "close", cookies_jar)
    """
        while True:
        print "%s\n%s\n%s" % selectcarLockState(terminal_id, car_id, cookies_jar)
        time.sleep(2)


    while not lockTaskIssued(car_id, terminal_id, "close", cookies_jar):
        time.sleep(1)
    """



if __name__ == "__main__":
    main()
