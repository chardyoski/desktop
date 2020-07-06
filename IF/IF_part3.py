import requests
from lxml import etree
import time
import re
import pandas as pd


def get_year_data(url,headers,i):
    content = requests.get(url=url, headers=headers)
    result = content.json()
    html = result['meta']['total_count']
    # data=result.xpath('/html/body/main/div[3]/div[1]/div[1]/a/div/span')
    # data = re.findall('<span class="filter-result-count">(.*?)</span>',result,re.DOTALL)
    # print(data)
    print(i,html)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

for i in range(1955,2021):
    # print(i)
    #按年份统计总获奖
    # url='https://ifworlddesignguide.com/api/v2/articles/design_excellence?cursor=0&lang=en&count=30&orderby=date&filter=%7B%22filters%22:[]%7D&time_min={0}&time_max={0}'.format(i)
    #按年份统计中国获奖
    # url='https://ifworlddesignguide.com/api/v2/articles/design_excellence?cursor=0&lang=en&count=30&orderby=date&filter=%7B%22filters%22:[%7B%22type%22:%22countries%22,%22ids%22:[45]%7D]%7D&time_min={0}&time_max={0}'.format(i)
    #按年份统计中国评委
    # url='https://ifworlddesignguide.com/api/v2/articles/jury?cursor=0&lang=en&count=30&orderby=date&filter=%7B%22filters%22:[%7B%22type%22:%22countries%22,%22ids%22:[%2245%22]%7D]%7D&time_min={0}&time_max={0}'.format(i)
    #按年份统计评委
    url='https://ifworlddesignguide.com/api/v2/articles/jury?cursor=0&lang=en&count=30&orderby=date&filter=%7B%22filters%22:[]%7D&time_min={0}&time_max={0}'.format(i)
    # print(url)
    # print(i)
    get_year_data(url,headers,i)
