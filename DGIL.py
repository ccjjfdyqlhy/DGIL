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

ver='1.0'
cwd=os.getcwd()

root=Tk()
root.title('DGIL '+ver)
root.geometry('800x400')
root.resizable(False,False)

global url
global inurl
byte=678700000

notebook = tkinter.ttk.Notebook(root)
starttab = tkinter.Frame()
downloadtab = tkinter.Frame()
setuptab = tkinter.Frame()
notebook.add(starttab, text='   启动   ')
notebook.add(downloadtab,text='   下载   ')
notebook.add(setuptab,text='   选项   ')
notebook.pack(padx=80, pady=40, fill=tkinter.BOTH, expand=True)

def check(context):
    if context.isdigit() or context == "":
        return True
    else:
        return False
def show():
    if xVariable.get() == 'YuanShen 3.1.0':
        inurl.insert(0,'https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220917165328_rVH9t4OWduSD75ye/YuanShen_3.1.0.zip')
        known_size=406846502.4
    elif xVariable.get() == 'YuanShen 3.2.0':
        inurl.insert(0,'https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20221024103540_fp3L3cHoDpo9eNeT/YuanShen_3.2.0.zip')
        known_size=407000000
    elif xVariable.get() == 'YuanShen 3.0.0':
        inurl.insert(0,'https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220815143702_i3RDKzdbDWGYYfZZ/YuanShen_3.0.0.zip')
        known_size=407000000
    else:
        print('[ERROR]Variable not definded')
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
        showinfo('DGIL - 提示','主要文件解包成功！你的游戏已经可以直接启动。\n如果想手动下载语音包，请使用终端中的链接。')
        print('语音包下载:\n3.2:[https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20221024103540_fp3L3cHoDpo9eNeT/Audio_Chinese_3.2.0.zip]\n3.1:[https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220917165328_rVH9t4OWduSD75ye/Audio_Chinese_3.1.0.zip]\n3.0:[https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220815143702_i3RDKzdbDWGYYfZZ/Audio_Chinese_3.0.0.zip]')
    except:
        showwarning('DGIL - 警告','找不到文件.\n前往下载选项卡下载安装包！')
def decompiledaudio():
    print('='*20+'解压中，切勿关闭程序和终端'+'='*20)
    try:
        unpack('./Audio_Chinese.dspck')
        showinfo('DGIL - 提示','语音文件解包成功！')
    except:
        showwarning('DGIL - 警告','找不到文件.')
        print('语音包下载:\n3.2:[https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20221024103540_fp3L3cHoDpo9eNeT/Audio_Chinese_3.2.0.zip]\n3.1:[https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220917165328_rVH9t4OWduSD75ye/Audio_Chinese_3.1.0.zip]\n3.0:[https://autopatchcn.yuanshen.com/client_app/download/pc_zip/20220815143702_i3RDKzdbDWGYYfZZ/Audio_Chinese_3.0.0.zip]')
def dslwelcome():
    dw=showinfo('DGIL - 关于','Darkstar Genshin Impact Launcher '+ver+'\n版权所有。Jeffery Darkstar, 2022')
def start():
    try:
        f=open(cwd+'/DGIL.cfg','r')
        gamingroute=f.read()
        print('GAMING ROUTE GET: '+gamingroute)
        try:
            root.withdraw()
            print('游戏启动！\n你现在可以关闭这个窗口了......')
            os.system(gamingroute)
        except KeyboardInterrupt:
            root.deiconify()
    except FileNotFoundError:
        showinfo('DGIL - 启动失败','未检测到指定的游戏文件.\n转到选项——设置来更改此项...')
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
com["value"] = ("YuanShen 3.2.0","YuanShen 3.1.0","YuanShen 3.0.0")
com.current(0)
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

routelabel=tkinter.Label(setuptab,text='自定义游戏路径：')
routelabel.pack()
def getroute():
    f_path = '"'+filedialog.askopenfilename()+'"'
    print('File route got: ', f_path)
    f=open(cwd+'/DGIL.cfg','w')
    f.write(f_path)
    print('data writed')
routeentry=tkinter.Button(setuptab,text='     点击选择游戏主执行文件(YuanShen.exe)     ',command=getroute)
routeentry.pack()
speedlabel=tkinter.Label(setuptab,text='最高下载速度限制(B/s)：\n启动时的默认值：678700000')
speedlabel.pack()
speedscale=tkinter.Scale(setuptab, from_=1024, to=1073741824, orient="horizontal", length=700)
speedscale.pack()
speedlabel1=tkinter.Label(setuptab,text='注意：如果你把滑块调到滑轨的85%以上，下载将对你的电脑内存造成不可挽回的伤害。\n除非你安装的是≥16G的内存，或者这个程序在超算上运行。')
speedlabel1.pack()

def confirmsetup():
    speedlimit=speedscale.get()
    byte=speedlimit
    print('New settings applied!')
confirmsetupbt=tkinter.Button(setuptab,text='     应用     ',command=confirmsetup)
confirmsetupbt.pack()

def startall():
    start()

startbutton=Button(starttab,text='          启动游戏          ',height='3',command=startall)
startbutton.pack()
root.mainloop()
