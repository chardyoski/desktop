import requests
from bs4 import BeautifulSoup
from lxml import etree
import requests
import csv
import pandas as pd


import time
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'''.split("\n")


def get_url(target,headers):

    content=requests.get(url=target,headers=headers)
    time.sleep(3)
    # content.encoding = 'ascii'
    # print(content.text)
    result = etree.HTML(content.content)
    # print(result.text)
    project_name=result.xpath('//div[@class="item-title"]/a/text()')
    '''项目名称'''
    # project_name = result.xpath(' /html/body/div/div[7]/div/div/main/article/div[3]//div[1]/div[2]/a/text()')
    '''代号'''
    code=result.xpath('//div[@class="item-summary"]/text()')
    '''状态'''
    status=result.xpath('//div[@class="item-meta"]/div[1]/span[2]/text()')
    '''日期'''
    date=result.xpath('//span[@class="date-display-single"]/text()')
    # print(project_name,code,status,date)

    test=result.xpath("/html/body/div/div[7]/div/div/main/article/div[3]/div[1]/div[2]/a/text()")
    if date is None:
        date='Not available'
    print("project_name:",project_name,"code:",code,'status:',status,'date:',date)


    # all.append(project_name)
    # all.append(code)
    # all.append(status)
    # all.append(date)
    return project_name,code,status,date


if __name__ == '__main__':
    headers ='''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: __cfduid=d64dee7212d254cd75542d37ae593dbf31594011597; _gcl_au=1.1.1932400524.1594011603; _ga=GA1.2.284661161.1594011603; _gid=GA1.2.2017489707.1594011603; has_js=1; o_user_session_adb=c3f2683b-c7d2-4355-8cfa-28de160673ad; o_new_user_adb=true
if-modified-since: Mon, 06 Jul 2020 05:34:05 GMT
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'''.split('\n')
    headers = {i.split(":")[0]: i.split(":")[1].strip() for i in headers}
    print(headers)
    Project_name=[]
    Code=[]
    Status=[]
    Date=[]
    for i in range(0,495):
        if i==0:
            target='https://www.adb.org/projects?page'
        else:
            target='https://www.adb.org/projects?page={0}'.format(i)



        project_name,code,status,date,=get_url(target,headers)
        Project_name.append(project_name)
        Code.append(code)
        Status.append(status)
        Date.append(date)

    Columns = ['project name', '代号','status','Approval Date']

    data=pd.concat([Project_name,Code,Status,Date],axis=1)
    data =data(columns=Columns)
    data.to_excel('测试.xlsx')

