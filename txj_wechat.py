# -*- coding: utf-8 -*-

from txj_spider import *
import sys
import itchat
reload(sys)
sys.setdefaultencoding('utf8')
itchat.auto_login()
cookies_jar, opener_rtn = installOpener()
loginWebsite(cookies_jar)

def appendLog(LogText):
    fp = open("log.txt", "a")
    fp.write(LogText + "\n")
    fp.close()

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    log_str = "Time" + getTick() + "  From:" + msg["FromUserName"] + "  Message:" + msg["Text"]
    print log_str
    appendLog(log_str)
    if msg["Text"].upper() == "HELP":
        return help_doc
    if msg["Text"][:3] != "CMD":
        return None
    try:
        message_case = msg['Text'].split(",")
        assert message_case[0] == "CMD"
        opr = message_case[1]
        terminal_id = message_case[2]
        if opr == "I":
            return getCarID(terminal_id, cookies_jar)
        car_id = message_case[3]
        if opr == "A":
            return lockTaskIssuedReason(car_id, terminal_id, "activation", cookies_jar)
        elif opr == "C":
            return lockTaskIssuedReason(car_id, terminal_id, "close", cookies_jar)
        elif opr == "L":
            return lockTaskIssuedReason(car_id, terminal_id, "lock", cookies_jar)
        elif opr == "U":
            return lockTaskIssuedReason(car_id, terminal_id, "unlock", cookies_jar)
        elif opr == "Q":
            Details, Code, Status = selectcarLockState(terminal_id, car_id, cookies_jar)
            return "状态：\n%s\n\n状态代码：\n%s\n\n状态详细（不一定准确）：\n%s" % (Status, Code, Details)
        else:
            return "格式正确，但是并不能解析的指令，请随便给我发几句话（比如“我爱你”之类）获得指南。"
    except Exception, e:
        print e.message
        try:
            loginWebsite(cookies_jar)
            print "重新登陆成功！"
        except:
            print "登录账号失败！"
        return "无法识别您的指令，尝试输入HELP(大小写均可)获取文档。\n如果您是和我聊天，请无视这一句。"
itchat.run()
