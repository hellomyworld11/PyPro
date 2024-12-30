import pymssql
import os
import xlrd
# os.environ['TDSDUMP'] = 'stdout'

class Sqlserver:
    ip = ''
    user = ''
    pd = ''
    database = ''
    db = object()
    tables = []

    def __init__(self, ip, iuser, ipd, idata):
        self.ip = ip
        self.user = iuser
        self.pd = ipd
        self.database = idata
        self.cursor = object()

    def __del__(self):
        self.db.close()

    def connect(self):
        # 打开数据库连接
        try:
            self.db = pymssql.connect(server = self.ip,
                                 user = self.user,
                                 password = self.pd,
                                 database = self.database)

            if self.db:
                print("连接成功")
                self.cursor = self.db.cursor()
                self.__GetTables()
            else:
                print("连接失败")
        except pymssql.Error as e:
            print(f"Error: {e}")

    def CreateTable(self, tablename, headers=[]):
        headerssize = len(headers)
        if headerssize == 0:
            return None
        strsql = f'create table {tablename} ('
        for index, colname in enumerate(headers):
            strsql+= f'{colname} nvarchar(max)'
            if index+1 < headerssize:
                strsql+= ','
        strsql+=')'
        print(strsql)
        self.cursor.execute(strsql)
        self.db.commit()

    def IsHaveTable(self, tablename):
        if tablename in self.tables:
            return True
        return False

    def __GetTables(self):
        strsql = "select name from sys.tables"
        self.cursor.execute(strsql)
        tables = self.cursor.fetchall()
        print("table num : " + str(len(tables)))
#       print(tables)
        print(tables)
        for name in tables:
            print(name[0])
            self.tables.append(name[0])

    def __GetTableCols(self, tablename):
        strsql = f"select  count (*)  from  syscolumns s   where  s.id = object_id( '{tablename}' );"
        self.cursor.execute(strsql)
        cols = self.cursor.fetchall()
        print(cols[0][0])
        return cols[0][0]

    def Import(self, tablename, datas):
        # 列数
        if len(datas) == 0:
            return False
        tablecols = self.__GetTableCols(tablename)
        if tablecols != len(datas[0]):
            print('列数不一样')
            return False

        strsub = '('
        for i in range(0, tablecols):
            strsub+='%s'
            if i+1 < tablecols:
                strsub+=','
        strsub += ')'

        strsql = f'insert into {tablename} values{strsub}'
        print(strsql)
        self.cursor.executemany(strsql, datas)
        self.db.commit()

def main():
    cli = Sqlserver('120.0.0.1', '111', '222', 'data')
    cli.connect()
    list = [(1, '2', 3, 'he'), (200, '2', 10.0, '111')]
    cli.Import('testimport', list)

if __name__ == '__main__':
    main()