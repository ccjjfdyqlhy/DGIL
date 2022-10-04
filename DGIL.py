import tkinter
from tkinter.messagebox import *
import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
import os
import math
import zipfile
import requests
import subprocess
import time

ver='0.2'
cwd=os.getcwd()

root=Tk()
root.title('DGIL '+ver)
root.geometry('800x400')
root.resizable(False,False)

global url
global inurl
byte=5242880

notebook = tkinter.ttk.Notebook(root)
starttab = tkinter.Frame()
downloadtab = tkinter.Frame()
connecttab = tkinter.Frame()
notebook.add(starttab, text='   启动   ')
notebook.add(downloadtab,text='   下载   ')
notebook.pack(padx=80, pady=40, fill=tkinter.BOTH, expand=True)
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
        try:
            subprocess.run([cwd+'\Genshin Impact Game\YuanShen.exe'])
        except KeyboardInterrupt:
            root.deiconify()
    except:
        showinfo('DGIL - 启动失败','未检测到安装的游戏文件.')
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

startbutton=Button(starttab,text='          启动游戏          ',height='3',command=start)
startbutton.pack()
root.mainloop()