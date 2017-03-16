# -*- coding: utf-8 -*-

from txj_spider import *
import sys
import itchat
reload(sys)
sys.setdefaultencoding('utf8')
itchat.auto_login()
cookies_jar, opener_rtn = installOpener()
#loginWebsite(cookies_jar)

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    try:
        message_case = msg['Text'].split(",")
        assert message_case[0]=="CMD"
        opr = message_case[1]
        terminal_id = message_case[2]
        car_id = message_case[3]
        if opr=="A":
            return lockTaskIssuedReason(car_id, terminal_id, "activation", cookies_jar)
        elif opr=="C":
            return lockTaskIssuedReason(car_id, terminal_id, "close", cookies_jar)
        elif opr=="L":
            return lockTaskIssuedReason(car_id, terminal_id, "lock", cookies_jar)
        elif opr=="U":
            return lockTaskIssuedReason(car_id, terminal_id, "unlock", cookies_jar)
        elif opr=="Q":
            return "Status:%s\nCode:%d" % selectcarLockState(terminal_id, car_id, cookies_jar)
    except:
        try:
            loginWebsite(cookies_jar)
        except:
            print "登录失败，妈卖批~"
        return """
指令错误或者执行错误，请使用如下指令（或者重试）：
CMD,[操作],[终端号],[车辆ID]
操作类型：
Q：查询锁车状态
A：激活锁车
C：关闭锁车
L：快捷锁车
U：快捷解锁
祝你身体愉快！
        """

itchat.run()