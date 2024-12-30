import pandas as pd
import os
import shutil

'''
data = {'列1': [1, 2, 3],
        '列2': ['司马光', '秦始皇', '李白'],
        '列3': [22, 25, 30]}

# table = pd.DataFrame(data)

# table = pd.read_excel("material.xls")

excel = pd.ExcelFile("material.xls")

print(excel.sheet_names)

table = excel.parse(excel.sheet_names[0])

#列数
aTuple  = table.shape
print(aTuple[1])

valuelist = table.values.tolist()
print(valuelist)
list_of_tuples = [tuple(sublist) for sublist in valuelist]
print(list_of_tuples)
'''

#返回 表头字典 数据字典
def getExcelData(excelpath):
   #强制改为xls
   tabledict = dict()
   headerdict = dict()
   file_name, file_extension = os.path.splitext(excelpath)
   if file_extension == '.xlsx':
#  shutil.copy(excelpath, 'testimport.xls')
       print('暂不支持读取xlsx')
       return headerdict, tabledict
#  excelpath = file_name + '.xls'

   excel = pd.ExcelFile(excelpath)
   if len(excel.sheet_names) == 0:
      print("excel have not data!")
      return headerdict, tabledict


   for name in excel.sheet_names:
       table = excel.parse(sheet_name=name, header=0)
       table = table.fillna(value='0')
       print(table.columns.tolist()) #表头
       tablelist = table.values.tolist()
       list_of_tuples = [tuple(sublist) for sublist in tablelist]
       tabledict[name] = list_of_tuples
       headerdict[name] = table.columns.tolist()
   return headerdict, tabledict


if __name__ == "__main__":
   headers, datas=  getExcelData("testimport.xls")
   print(datas)
   print(headers['testimport'])