import csv
import sqlite3
import tkinter
import tkinter.ttk
import os
from tkinter import messagebox

#sqlite数据库表快速转为csv 支持批量转换

window = None
e1 = None
l1 = None
l2 = None
combobox = None

def mkdir(path):

    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        print('dir exist')

def sqlitetocsv(sqlite1, table1 ,csv1 = 'mytable.csv'):
    # 连接SQLite数据库
    conn = sqlite3.connect(sqlite1)
    sqlitename = str(sqlite1)
    sqlitename = sqlitename.replace('.db', '')
    path = os.getcwd()
    mkdir(path + '\\'+ sqlitename)
    c = conn.cursor()

    csv1 = path +'\\{0}\\{1}.csv'.format(str(sqlitename), str(table1))
    # 查询数据
    str1 = 'SELECT * FROM {0}'.format(str(table1))
    c.execute(str1)
    # 打开CSV文件并写入数据
    with open(csv1, 'w', newline='') as f:
        writer = csv.writer(f)
        # 写入表头
        writer.writerow([i[0] for i in c.description]) #列表解析器
        # 写入数据
        writer.writerows(c)

    conn.close()

def getsqlitetables(sqlite1):
    print(sqlite1)
    conn = sqlite3.connect(sqlite1)
    cur = conn.cursor()
    cur.execute("select name from sqlite_master where type='table' order by name")
    # print(cur.fetchall())
    # return cur.fetchall()
    variable = []
    sets = cur.fetchall()
    for var in sets:
        list = var
        print(list[0])
        variable.append(list[0])
    conn.close()
    return variable

def start():
    print("进行转换...")
    global e1
    global combobox
    n1 = e1.get()  # 获取输入框1的值
    n2 = combobox.get()
    sqlitetocsv(n1, n2)

def startall():
    print("进行转换...")
    global e1
    n1 = e1.get()  # 获取输入框1的值

    tables = getsqlitetables(n1)
    for i in tables:
        sqlitetocsv(n1, i)

def inputdb(event=''):
    global e1
    global combobox
    n1 = e1.get()
    tables = getsqlitetables(n1)
    if len(tables) == 0:
        messagebox.showinfo('提示', '不存在或连接失败！')

    combobox["value"] = tables
   # combobox.pack(padx=5, pady=10)

def initDlg():
    global window  #想要修改全局变量
    global e1
    global l1
    global l2
    global combobox

    # 主窗口
    window = tkinter.Tk()
    # 设置窗口title
    window.title('sqlite转csv助手1.0')
    # 设置窗口大小
    window.geometry('300x80')

    # 定义输入框1
    e1 = tkinter.Entry(window, width=15)
    e1.bind('<Return>', inputdb)
    e1.pack()
    e1.place(x = 60,y =10,width = 100,height = 20)

    # 定义标签
    l2 = tkinter.Label(window, text='表名')
    l2.pack()
    l2.place(x=1, y=40, width=50, height=20)

    l1 = tkinter.Label(window, text='数据库')
    l1.pack()
    l1.place(x=1, y=10, width=50, height=20)

    #定义 组合框
    var = tkinter.StringVar()
    combobox = tkinter.ttk.Combobox(window, textvariable=var, value=('',))
    combobox.pack(padx=5, pady=10)
    combobox.place(x=60, y=40 , width=100, height=20)

    # 定义转换一张表button
    b = tkinter.Button(window,
                       text='转换',  # 按钮的文字
                       bg='pink',  # 背景颜色
                       width=15, height=2,  # 设置长宽
                       command=start  # 响应事件：关闭窗口
                       )
    b.pack()
    b.place(x = 200 ,y = 40,width= 60,height = 20)

    # button: 转换所有表
    ball = tkinter.Button(window,
                       text='转换所有',  # 按钮的文字
                       bg='yellow',  # 背景颜色
                       width=15, height=2,  # 设置长宽
                       command=startall  # 响应事件：关闭窗口
                       )
    ball.pack()
    ball.place(x = 200 ,y = 10,width= 60,height = 20)

    #初始化工作
    e1.insert('insert','test.db')
    # 显示主窗口
    window.mainloop()

if __name__ == "__main__":
    initDlg()

