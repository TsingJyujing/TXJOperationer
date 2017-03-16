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
txj_host = "http://www.sqtxj.com/"

api_selectcarLockState = txj_host + "systemManager/selectLockStatus.do?terminalId=%s&carId=%s"
api_lockTaskIssued_queryOnlineStatus = txj_host + "systemManager/checkLockEnabled.do?carId=%s&terminalId=%s"
api_lockTaskIssued_executeCommand = txj_host + "systemManager/lockTaskIssued.do?carId=%s&lockType=%s"
api_lockTaskIssued_oprs = set(["activation", "close", "unlock", "lock"])



