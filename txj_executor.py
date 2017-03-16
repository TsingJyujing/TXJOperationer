# -*- coding: utf-8 -*-

import Tkinter
from txj_spider import *
import tkMessageBox
import threading
from basic_libs import getTick


iter_max_times = 10
terminal_id = "1702281081"  # 1702241026
car_id = "57034724"  # 57034723
cookies_jar, opener_rtn = installOpener()
loginWebsite(cookies_jar)


def updateText(StringBuf):
    while True:
        time.sleep(2)
        T = getTick()
        des, r = selectcarLockState(terminal_id, car_id, cookies_jar)
        print_message = "Status:%s\nCode:%d\nTick:%s" % (des, r, T)
        StringBuf.set(print_message)
        print print_message

def genThread(StringBuf):
    print "Creating thread..."
    threading.Thread(target=updateText, args=(StringBuf,)).start()
    print "Create thread successfully."


def btnLock_Click():
    i = 0
    while not lockTaskIssued(car_id, terminal_id, "lock", cookies_jar):
        print "Error while locking %s, retrying..." % terminal_id
        time.sleep(2)
        i += 1
        if i >= iter_max_times:
            tkMessageBox.showinfo("Lock", "%s Lock failed." % terminal_id)
            return
    tkMessageBox.showinfo("Lock", "%s Lock successfully." % terminal_id)


def btnUnlock_Click():
    i = 0
    while not lockTaskIssued(car_id, terminal_id, "unlock", cookies_jar):
        print "Error while unlocking %s, retrying..." % terminal_id
        time.sleep(2)
        i += 1
        if i >= iter_max_times:
            tkMessageBox.showinfo("Unlock", "%s Unlock failed." % terminal_id)
            return
    tkMessageBox.showinfo("Unlock", "%s Unlock successfully." % terminal_id)


def btnClose_Click():
    i = 0
    while not lockTaskIssued(car_id, terminal_id, "close", cookies_jar):
        print "Error while closing %s, retrying..." % terminal_id
        time.sleep(2)
        i += 1
        if i >= iter_max_times:
            tkMessageBox.showinfo("Disable lock", "%s Disable lock failed." % terminal_id)
            return
    tkMessageBox.showinfo("Disable lock", "%s Disable lock successfully." % terminal_id)


def btnOpen_Click():
    i = 0
    while not lockTaskIssued(car_id, terminal_id, "activation", cookies_jar):
        print "Error while activation %s, retrying..." % terminal_id
        time.sleep(2)
        i += 1
        if i >= iter_max_times:
            tkMessageBox.showinfo("Enable lock", "%s Enable lock failed." % terminal_id)
            return
    tkMessageBox.showinfo("Enable lock", "%s Enable lock successfully." % terminal_id)


def main():
    Frm = Tkinter.Tk()

    btnLock = Tkinter.Button(Frm, text="Lock Vehicle", command=btnLock_Click)
    btnLock.pack()

    btnUnlock = Tkinter.Button(Frm, text="Unlock Vehicle", command=btnUnlock_Click)
    btnUnlock.pack()

    btnClose = Tkinter.Button(Frm, text="Disable Lock Vehicle", command=btnClose_Click)
    btnClose.pack()

    btnOpen = Tkinter.Button(Frm, text="Enable Lock Vehicle", command=btnOpen_Click)
    btnOpen.pack()

    StringBuf = Tkinter.StringVar()
    StringBuf.set("Status: Unknow\n\n Code:NaN")
    lbStatus = Tkinter.Label(Frm, textvariable=StringBuf, relief=Tkinter.RAISED)
    genThread(StringBuf)
    lbStatus.pack()

    Frm.mainloop()

if __name__ == "__main__":
    main()