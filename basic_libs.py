# -*- coding: utf-8 -*-
from configure import *
import re
import urllib2
import cookielib
import datetime
import time


def getTick():
    return datetime.datetime.now().isoformat(sep=" ")


def urlOpen(url, retry_times=3, referer="", cookie="", postdata=None):
    for i in range(retry_times):
        try:
            req_header = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Host': re.findall('://.*?/', url, re.DOTALL)[0][3:-1],
                'Referer': referer,
                "Cookie": cookie
            }
            return urllib2.urlopen(
                urllib2.Request(url, None, req_header),
                postdata, request_timeout
            ).read()
        except Exception, e:
            print "Error while reading URL: ", e.message, "retrying..."
    print "Error while reading:", url


def installOpener():
    cj = cookielib.CookieJar()
    hcook = urllib2.HTTPCookieProcessor(cj)
    ortn = urllib2.build_opener(hcook)
    urllib2.install_opener(ortn)
    return cj, ortn


def generateCookiesString(cookie):
    cookie_use = []
    for item in cookie:
        cookie_use.append("%s=%s" % (item.name, item.value))
    return "; ".join(cookie_use)


def writeRaw(filename, data):
    f = open(filename, 'wb')
    f.write(data)
    f.close()

