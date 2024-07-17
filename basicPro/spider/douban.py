import requests
import io
import re
import time
import random
import openpyxl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

workbook = openpyxl.Workbook()
sheet = workbook.active

def get_read_top250(url):

    for page in range(1, 11):
        tempurl = url
        num = (page-1)*25
        tempurl += f'?start={num}'
        print(num)

        get_read_top250_apage(tempurl, page)
        break
        time.sleep(random.random() * 4 + 1)

    workbook.save("1.xlsx")


def get_read_top250_apage(url, page):
    print("url: " + url + f'page: {page}')
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print("Get error")
        return None
    res.encoding = 'utf-8'
    text = res.text
#    print(text)
#   file = open("第%d页"%(page), "w", encoding='utf-8')
#    file.write(text)
#    file.close()

#    正则解析   这里留下一个疑问，为什么匹配不到豆瓣top250
#    已解决 对于特殊符号需要转义
    # <a href="https://book.douban.com/subject/1007305/"
    # onclick="&quot;moreurl(this,{i:'0'})&quot;" title="红楼梦">红楼梦</a>
    pattern = re.compile(r'<a href="https:\/\/book.douban.com\/subject\/[\d]+\/" onclick=&#[0-9]+;moreurl\(this,\{i:&#[0-9]+;[0-9]+&#[0-9]+;\}\)&#[0-9]+; title="[\u4e00-\u9fa5]+"[\s]*>([^&]*?)</a>')

    titles = pattern.findall(text)

    print("len " + str(len(titles)))
   # 写入excel
    for title in titles:
        title = title.strip().replace(' ', '').replace('\n', '')
        # 如果有副标题则进行匹配
        childpahttern = re.compile(r'.*<spanstyle=".*">:([^&]*?)</span>')
        childtitle = childpahttern.findall(title)
        strtitle = ""
        if len(childtitle) > 0:
            strtitle = childtitle[0]
        sheet.insert_rows(1)

        print('strtitle: '+ strtitle)
        print(title + strtitle)
        sheet['A1'] = title + strtitle



def test_reg(src):

    src = "<a href=\"https://book.douban.com/subject/1007305/\" onclick=\"&quot;moreurl(this,{i:'0'})&quot;\" title=\"红楼梦\">\
                红楼梦\
                            \
                            \
              </a>"

    pattern = re.compile(r'<a href=".*" .*" title=".*">([^&]*?)</a>')

    dst = pattern.findall(src)

    for title in dst:
        print(title)




if __name__ == '__main__':
    url = "https://book.douban.com/top250"
    url1 = "https://www.baidu.com"
    get_read_top250(url)
 #   test_reg("")