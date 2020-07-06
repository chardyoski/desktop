import pandas as pd
import csv
import xlrd
import requests
from lxml import etree
import re
import time
def get_information(url,headers):
    content = requests.get(url=url,headers=headers)
    # print(content.text)
    # result = etree.HTML(content.content)
    result=content.text


    Amount=re.findall(">USD (.*?)</td>", result, re.DOTALL)



    # tr=re.findall("<td><table>(.+?)</table></td>",result,re.DOTALL)
    # trs = result.xpath('//*[@class="article"]/table[1]/tbody/tr')
    #
    # for tr in trs:
    #     Amount=tr.xpath('./tr/tr[6]/td[2]/table/tbody/tr[2]/td[2]/text()')
    #     print(Amount)

#      //*[@id="project-pds"]/div/div/div/table[1]/tbody/tr[5]/td[1]

#     tag=result.xpath()
# #    //*[@id="project-pds"]/div/div/div/table[1]/tbody/tr[6]/td[2]/table/tbody
#     if tag =='Source of Funding / Amount' or tag=='funding':
#         Amount=''
#     else:
#         Amount='error'

    return Amount
if __name__=='__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    # url='https://www.adb.org/projects/46374-002/main#project-pds'
    # Amount=get_information(url, headers)
    # print(Amount)
    Amount=[]



    res=pd.read_excel('ADB补充.xlsx')
    start=time.time()
    for i in res['url']:
        amount=get_information(i,headers)
        Amount.append(amount)
        print(i)
        print(amount)
    end=time.time()

    data=pd.DataFrame({'Amount':Amount,'url':res['url']})

    data.to_excel('Amount.xlsx',mode='a')
    print(end-start)
