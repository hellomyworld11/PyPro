import xlrd
import pymssql
import tkinter
import tkinter.ttk
import os
from tkinter import messagebox
from tkinter import filedialog
from excel import getExcelData
from sqlserver import Sqlserver
from tkinter import Checkbutton
from ttkbootstrap import Style

window   = None
pathedit = None
pdedit   = None
dataedit = None
ipedit   = None
useredit = None

f_path = ''
checkvar = None
#添加 sqlsrver数据库设置信息
# 定义地址  用户名 密码 数据库


#选择路径
def SelFile():
    global pathedit
    global f_path
    print("选择文件...")
    f_path = filedialog.askopenfilename(title='选择一个excel', initialdir=r'F:\\mycode\\pytest\\little\\sqlser')
    print('\n获取的文件地址：', f_path)
    pathedit.delete(0, tkinter.END)
    pathedit.insert(0, f_path)

#导入
def start():
    print("导入...")
    ip = ipedit.get()
    user = useredit.get()
    pd = pdedit.get()
    dbname = dataedit.get()
    print(f_path)
    if len(f_path) == 0:
        print("文件路径为空")
        return None
    isCreate = checkvar.get()
    print('isCreate: ' + str(isCreate))

    headerdatas, tabledatas= getExcelData(f_path)
    print(tabledatas)
    cli = Sqlserver(ip, user, pd, dbname)
    cli.connect()
    for key, value in tabledatas.items():
        if cli.IsHaveTable(key):
           cli.Import(key, value)
        elif isCreate:
           cli.CreateTable(key, headerdatas[key])
           cli.Import(key, value)

def InitDlg():
    global window
    global pdedit
    global pathedit
    global dataedit
    global ipedit
    global useredit
    global checkvar

    window = tkinter.Tk()
    # 设置窗口title
    window.title('excel导入到sqlserver助手1.0  by xupan')
    # 设置窗口大小
    window.geometry('500x100')
    window.resizable(0, 0)

    #定义标签
    iplabel = tkinter.Label(window, text='地址')
    iplabel.pack()
    iplabel.place(x=1, y=10, width=40, height=20)
    ipedit = tkinter.Entry(window, width=25)
    ipedit.pack()
    ipedit.place(x=40, y=10, width=100, height=20)
    ipedit.insert('insert', '127.0.0.1')

    userlabel = tkinter.Label(window, text='用户名')
    userlabel.pack()
    userlabel.place(x=150, y=10, width=40, height=20)
    useredit = tkinter.Entry(window, width=25)
    useredit.pack()
    useredit.place(x=200, y=10, width=100, height=20)
    useredit.insert('insert', '111')

    pdlabel = tkinter.Label(window, text='密码')
    pdlabel.pack()
    pdlabel.place(x=150, y=40, width=40, height=20)
    pdedit = tkinter.Entry(window, width=25, show="*")
    pdedit.pack()
    pdedit.place(x=190, y=40, width=100, height=20)
    pdedit.insert('insert', '222')

    datalabel = tkinter.Label(window, text='数据库')
    datalabel.pack()
    datalabel.place(x=1, y=40, width=40, height=20)
    dataedit = tkinter.Entry(window, width=25)
    dataedit.pack()
    dataedit.place(x=50, y=40, width=100, height=20)
    dataedit.insert('insert', 'data')

    # exel路径
    pathlabel = tkinter.Label(window, text='路径')
    pathlabel.pack()
    pathlabel.place(x=1, y=70, width=40, height=20)
    pathedit = tkinter.Entry(window, width=25)
    pathedit.pack()
    pathedit.place(x=40, y=70, width=250, height=20)

    b = tkinter.Button(window,
                       text='选择文件',  # 按钮的文字
                       bg='pink',  # 背景颜色
                       width=15, height=2,  # 设置长宽
                       command=SelFile  # 响应事件：关闭窗口
                       )
    b.pack()
    b.place(x=350, y=70, width=60, height=20)

    b = tkinter.Button(window,
                       text='导入',  # 按钮的文字
                       bg='pink',  # 背景颜色
                       width=15, height=2,  # 设置长宽
                       command=start  # 响应事件：关闭窗口
                       )
    b.pack()
    b.place(x=420, y=70, width=60, height=20)

    checkvar = tkinter.IntVar()
    createTablebox = Checkbutton(window, text='自动创建表', variable=checkvar)
    createTablebox.grid(row=1, sticky=tkinter.W)
    createTablebox.place(x=380, y=20)

    # 显示主窗口
    window.mainloop()

if __name__ == "__main__":
    InitDlg()