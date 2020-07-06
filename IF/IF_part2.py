import requests
from lxml import etree
import time
import re
import pandas as pd

# data=pd.read_excel('IF奖.xlsx')
# for url in data['url']:
#     pass

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

# url='https://ifworlddesignguide.com/entry/249603-100-home-changes-more-than-100'
def get_information(url,headers):
        result = requests.get(url=url, headers=headers)
        content=result.text
        #获取客户或者生产商Client / Manufacturer
        # Client=re.findall(r'product-client-box-category copy-1">Client.*?product-client-box-description"(.*?)</p>',result,re.DOTALL)[0].replace('<br>','').replace(' ','').replace('>','').replace('\n','|')
        try:

            # tree = etree.HTML(content)
            #获取设计师或者设计团队
            Design = re.findall(r'<h2 class="product-client-box-headline headline-2">(.*?)</h2>', content, re.DOTALL)[1]

            # Design=re.findall(r'<p class="product-client-box-description">.*?<br><br>(.*?)</p>',content, re.DOTALL)[1]
            # '''<p class="product-client-box-description">
            #                     POSCO A&amp;C<br>
            #                                                     Seoul, South Korea<br>
            #                                                         <br>
            #                                                                 Keon-woo Kang, Jindalmee Choe, Hyunbok Lee, Jong eun Han, Chea young Kim, Hyo jung Kim, Youna Choi, Myung hwa Jeon, Young jin Kang, Kyoung rock Kim, Hye jin Um
            #                                                                                     </p>'''
            # Design=tree.xpath('//div[@class="row align-right"]/div[2]/div[1]/h2[@class="product-client-box-headline headline-2"]/text()')

            if Design:
                print(Design)
            else:
                print(url,'None')

        except Exception as e:
            print(e)
            print(url)
