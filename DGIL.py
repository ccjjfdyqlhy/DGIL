import tkinter
from tkinter.messagebox import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
import os
import math
import zipfile
import requests
import subprocess
import time
import pywintypes
import win32api
import win32con

ver='0.3'
cwd=os.getcwd()

def on_closing():
    win32api.RegCloseKey(regeditKey)
    root.destroy()

root=Tk()
root.title('DGIL '+ver)
root.geometry('800x400')
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW", on_closing)

global url
global inurl
byte=5242880

notebook = tkinter.ttk.Notebook(root)
starttab = tkinter.Frame()
downloadtab = tkinter.Frame()
setuptab = tkinter.Frame()
notebook.add(starttab, text='   启动   ')
notebook.add(downloadtab,text='   下载   ')
notebook.add(setuptab,text='   选项   ')
notebook.pack(padx=80, pady=40, fill=tkinter.BOTH, expand=True)

try:
    screenWidth = win32api.GetSystemMetrics(0)
    screenHeight = win32api.GetSystemMetrics(1)
    regeditKey = win32api.RegOpenKey(
        win32con.HKEY_CURRENT_USER, r'Software\miHoYo\原神', 0, win32con.KEY_ALL_ACCESS)
    regHeight = win32api.RegQueryValueEx(
        regeditKey, 'Screenmanager Resolution Height_h2627697771')[0]
    regWidth = win32api.RegQueryValueEx(
        regeditKey, 'Screenmanager Resolution Width_h182942802')[0]
    regFullScreen = win32api.RegQueryValueEx(
        regeditKey, 'Screenmanager Is Fullscreen mode_h3981298716')[0]
except:
    exit(1)

def check(context):
    if context.isdigit() or context == "":
        return True
    else:
        return False
def show():
    if xVariable.get() == 'YuanShen 3.1.0':
        inurl.insert(0,'https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220917165328_rVH9t4OWduSD75ye/YuanShen_3.1.0.zip')
        known_size=406846502.4
    else:
        inurl.insert(0,'https://autopatchhk.yuanshen.com/client_app/download/pc_zip/20220917165430_NyMmj1Ta9KlZKgCZ/GenshinImpact_3.1.0.zip')
        known_size=4068693948.8
    url=inurl.get()
    getgamebutton["state"]="disabled"
    r = requests.get(url, stream = True)
    with open("main.dspck", "wb") as Pypdf:
        for chunk in r.iter_content(chunk_size = byte):
            if chunk:
                Pypdf.write(chunk)
                file_size = os.path.getsize(cwd+r'\main.dspck') 
                i=math.floor(file_size/known_size)
                progressbarOne['value'] = i
                progress.config(text=str(i)+'%')
                root.update()
                if i == 100:
                    progress.config(text='校验下载资源')
                    tkinter.messagebox.showinfo('DGIL','下载完成.\n转到[启动器>从特定包安装Genshin Impact]开始安装!')
def unpack(targetfile):
    with zipfile.ZipFile(targetfile) as zf:
        try:
            zf.extractall()
            print('\n[WARN]Unpack Successfully.')
        except zipfile.BadZipFile:
            print('\n[ERROR]Failed when unpacking dspck file')
def decompiled():
    print('='*20+'UNPACKING'+'='*20)
    try:
        unpack('./main.dspck')
        showinfo('DGIL - 提示','主要文件解包成功！')
        print('3.1语音包下载:[]')
    except:
        showwarning('DGIL - 警告','找不到文件.\n前往下载选项卡下载特定安装包或使用官方启动器安装！')
def decompiledaudio():
    print('='*20+'UNPACKING'+'='*20)
    try:
        unpack('./Audio_Chinese.dspck')
        showinfo('DGIL - 提示','语音文件解包成功！')
    except:
        showwarning('DGIL - 警告','找不到文件.')
def dslwelcome():
    dw=showinfo('DGIL - 关于','Darkstar Genshin Impact Launcher '+ver+'\n版权所有。Jeffery Darkstar, 2022')
def start():
    try:
        f=open(cwd+'/DGIL.cfg','r')
        gamingroute=f.read()
        print('GAMING ROUTE GET: '+gamingroute)
        try:
            root.withdraw()
            print('Game Launch!')
            os.system(gamingroute)
        except KeyboardInterrupt:
            root.deiconify()
    except FileNotFoundError:
        showinfo('DGIL - 启动失败','未检测到指定的游戏文件.\n转到选项一设置')
        root.deiconify()
menu1 = Menu(starttab, tearoff=0)
menu1.add_command(label="从特定包安装Genshin Impact",command=decompiled)
menu1.add_command(label="安装语音包",command=decompiledaudio)
mebubar = Menu(starttab)
mebubar.add_command(label="DGIL", command=dslwelcome)
mebubar.add_cascade(label="启动器", menu=menu1)
mebubar.add_command(label="退出", command=root.quit)
root.config(menu=mebubar)

title=Label(starttab,text=' ',font=('微软雅黑','20'))
title.pack(anchor='n')

title=Label(downloadtab,text='安装包下载',font=('微软雅黑','20'))
title.pack(anchor='n')
urltext1=tkinter.Label(downloadtab,text='从列表中选择一个版本下载')
urltext1.pack()
xVariable = tkinter.StringVar()
com = ttk.Combobox(downloadtab,textvariable=xVariable)
com.pack()
com["value"] = ("Genshin Impact 3.1.0","YuanShen 3.1.0")
com.current(1)
def xFunc(event):
    print('Download version chosen:'+xVariable.get())
com.bind("<<ComboboxSelected>>", xFunc)

urltext=tkinter.Label(downloadtab,text='或将DSGenshin官方发布的下载链接粘贴到下方')
urltext.pack()
inurl=tkinter.Entry(downloadtab,width=20)
inurl.pack()
progressbarOne = tkinter.ttk.Progressbar(downloadtab,length=280)
progressbarOne.pack(pady=20)
progressbarOne['maximum'] = 100
progressbarOne['value'] = 0
progress=tkinter.Label(downloadtab,text='0%')
progress.pack()
getgamebutton = tkinter.Button(downloadtab, text='          获取游戏          ', command=show)
getgamebutton.pack(pady=5)

widthLabel = tkinter.Label(starttab, text='宽 Width')
widthLabel.pack()
width = tkinter.StringVar()
widthEntry = tkinter.Entry(starttab, show=None, textvariable=width)
widthEntry.pack()
width.set(regWidth)
heightLabel = tkinter.Label(starttab, text='高 Height')
heightLabel.pack()
height = tkinter.StringVar()
heightEntry = tkinter.Entry(starttab, show=None, textvariable=height)
heightEntry.pack()
height.set(regHeight)
flag = tkinter.IntVar()
fullscreenCheckbutton = tkinter.Checkbutton(
    starttab, text='全屏显示 FullScreen', variable=flag, onvalue=1, offvalue=0)
fullscreenCheckbutton.pack()
flag.set(regFullScreen)
def main():
    global regWidth
    global regHeight
    global regFullScreen
    widthNum = width.get()
    heightNum = height.get()
    isfullScreen = int(bool(flag.get()))
    if check(widthNum) and check(heightNum):
        widthNum = int(widthNum)
        heightNum = int(heightNum)
        if not (int(widthNum) <= screenWidth and int(heightNum) <= screenHeight):
            tkinter.messagebox.showerror(
                title='Error', message='Width/Height 超出屏幕尺寸.')
            return
    else:
        tkinter.messagebox.showerror(
            title='Error', message='Width/Height Error.')
        return
    msgbox = False
    if widthNum != regWidth:
        try:
            win32api.RegSetValueEx(
                regeditKey, 'Screenmanager Resolution Width_h182942802', 0, win32con.REG_DWORD, widthNum)
            regWidth = win32api.RegQueryValueEx(
                regeditKey, 'Screenmanager Resolution Width_h182942802')[0]
            msgbox = True
        except:
            tkinter.messagebox.showerror(
                title='Error', message='Regedit I/O Error.')
            exit(1)
    if heightNum != regHeight:
        try:
            win32api.RegSetValueEx(
                regeditKey, 'Screenmanager Resolution Height_h2627697771', 0, win32con.REG_DWORD, heightNum)
            regHeight = win32api.RegQueryValueEx(
                regeditKey, 'Screenmanager Resolution Height_h2627697771')[0]
            msgbox = True
        except:
            tkinter.messagebox.showerror(
                title='Error', message='Regedit I/O Error.')
            exit(1)
    if isfullScreen != regFullScreen:
        try:
            win32api.RegSetValueEx(
                regeditKey, 'Screenmanager Is Fullscreen mode_h3981298716', 0, win32con.REG_DWORD, isfullScreen)
            regFullScreen = win32api.RegQueryValueEx(
                regeditKey, 'Screenmanager Is Fullscreen mode_h3981298716')[0]
            msgbox = True
        except:
            tkinter.messagebox.showerror(
                title='Error', message='Regedit I/O Error.')
            exit(1)
    if msgbox:
        tkinter.messagebox.showinfo(title='Info', message='Success!')

routelabel=tkinter.Label(setuptab,text='自定义游戏路径：')
routelabel.pack()
def getroute():
    f_path = '"'+filedialog.askopenfilename()+'"'
    print('File route got: ', f_path)
    f=open(cwd+'/DGIL.cfg','w')
    f.write(f_path)
    print('data writed')
routeentry=tkinter.Button(setuptab,text='     点击选择游戏主执行文件     ',command=getroute)
routeentry.pack()
speedlabel=tkinter.Label(setuptab,text='最高下载速度限制(B/s)：')
speedlabel.pack()
speedscale=tkinter.Scale(setuptab, from_=1024, to=5242880, orient="horizontal", length=700)
speedscale.pack()

def confirmsetup():
    speedlimit=speedscale.get()
    byte=speedlimit
    print('New settings applied!')
confirmsetupbt=tkinter.Button(setuptab,text='     应用     ',command=confirmsetup)
confirmsetupbt.pack()

def startall():
    main()
    start()

startbutton=Button(starttab,text='          启动游戏          ',height='3',command=startall)
startbutton.pack()
root.mainloop()
