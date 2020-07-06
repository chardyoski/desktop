import requests
from lxml import etree
import time
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

# 原始url
# url='https://ifworlddesignguide.com/api/v2/articles/design_excellence?cursor=30&lang=en&count=30&orderby=date&filter=%7B%22filters%22:[%7B%22type%22:%22countries%22,%22ids%22:[%2245%22]%7D]%7D'

def get_information(url,headers):
    content = requests.get(url=url,headers=headers)
    # print(content)
    answer=content.json()
    Html=[]
    Name=[]
    Title=[]
    Type=[]
    for i in range(0,30):
        #链接
        html=answer['data'][i]['href']
        Html.append(html)
        #名字
        name=answer['data'][i]['headline']
        Name.append(name)
        # 奖项时间
        title = answer['data'][i]['awardlogo']['title']
        Title.append(title)

        # item_type=answer['']['']['']
        # Type.append(item_type)
        print(html,name,title,sep='嘁')

    data = pd.DataFrame({'html': Html, 'Name':Name,'Title':Title})

    data.to_excel('IF获奖.xlsx')

# get_information(url, headers)

for j in range(0,3120,30):
    time.sleep(1)
    url='https://ifworlddesignguide.com/api/v2/articles/design_excellence?cursor={0}&lang=en&count=30&orderby=date&filter=%7B%22filters%22:[%7B%22type%22:%22countries%22,%22ids%22:[%2245%22]%7D]%7D'.format(j)
    get_information(url, headers)
