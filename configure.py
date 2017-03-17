# -*- coding: utf-8 -*-
request_timeout = 60
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " + \
             "AppleWebKit/537.36 (KHTML, like Gecko) " + \
             "Chrome/42.0.2311.135 " + \
             "Safari/537.36 " + \
             "Edge/12.10240"

XML_decoder = 'lxml'

user_name = "znscsc"
user_pwd = None
# txj_host = "http://www.sqtxj.com/"
txj_host = "http://172.16.9.2/"
api_selectcarLockState = txj_host + "systemManager/selectLockStatus.do?terminalId=%s&carId=%s"
api_lockTaskIssued_queryOnlineStatus = txj_host + "systemManager/checkLockEnabled.do?carId=%s&terminalId=%s"
api_lockTaskIssued_executeCommand = txj_host + "systemManager/lockTaskIssued.do?carId=%s&lockType=%s"
api_lockTaskIssued_oprs = set(["activation", "close", "unlock", "lock"])
api_loadCarInfo = txj_host + "systemManager/loadCarInfo.do?carInfoVo.vinCode=&carInfoVo.carNo=&carInfoVo.simCard=&carInfoVo.terminalId=%s&carInfoVo.lockState=99&insertStartTime=&insertEndTime="

help_doc = """天行健锁车测试微信客户端使用文档
————————
请使用如下指令：
CMD,[操作],[终端号],[车辆ID]
操作类型：
Q：查询锁车状态
A：激活锁车
C：关闭锁车
L：快捷锁车
U：快捷解锁
————————
新增查询CarID的功能，指令为：
CMD,I,[终端号]
终端号可以只输入一部分，举个栗子：
CMD,I,1702241
但是如果查出的终端号太多请补全一些再重试
执行连续出错或者虽然成功但是无效时请执行此指令检查CarID是否正确！
————————
如果出错或者没有响应，请检查输入以后再试一次！
请使用大写和英文逗号，严格按照说明使用！"""




