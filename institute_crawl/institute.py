import requests
import time
import pandas as pd
import os

class Crawl:
    def __init__(self,field,institution,stamp):
        # self.stamp = int((time.time() + 1) * 1000)
        self.institution=institution
        self.field=field
        # self.original='https://esi-clarivate-com.ezproxy.cul.columbia.edu/IndicatorsDataAction.action?_dc={0}&type=trendsGraph&sort=citations&article_UT=&author=&articleTitle=&researchField={1}&institution={2}&journal=&researchFront=&territory=&docType=Top&year=&page=1&start=0&limit=25'.format(stamp, field, institution)
        self.original='http://fbzzde53972df5b34b0ca817704053506eebsx9v00ok5ou906n5q.faia.ncu.cwkeji.cn:8080/IndicatorsDataAction.action?_dc={0}&type=trendsGraph&sort=citations&article_UT=&author=&articleTitle=&researchField={1}&institution={2}&journal=&researchFront=&territory=&docType=Top&year=&page=1&start=0&limit=25'.format(stamp, field, institution)
        self.url=Crawl.get_information(self)

    def get_information(self):
        #得到url地址
        url=self.original
        return url
        # try:
        #     all = requests.get(url, headers=headers,timeout=30)
        #     if all.json():
        #         content = all.json()
        #         result=content['convertedData']
        #         df = pd.DataFrame(result['convertedData'])
        #         return df
        #     else:
        #         print('未获取到json:',i,j)
        # except:
        #     print('异常:',i,j)
        # return url



    # def get_path(self):
    #     data=self.df
    #     #根据机构建立文件夹
    #     data.to_excel()
    #     #根据领域建立文件
    #     pass

if __name__=='__main__':

    headers = '''AAccept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: CWJSESSIONID=7EFF44FB54357D9E3756D54E24F253A3; cwsid=c6fbb7d5736b4e51; _sp_ses.1acd=*; _sp_id.1acd=26e4c8d2-08d5-4cb2-afe5-f6f7aad71190.1568007540.1.1568007554.1568007540.28cee273-3162-4dfb-8d5b-640e15ddcb7f; esi.isLocalStorageCleared=true; _ga=GA1.2.333028641.1568007567; _gid=GA1.2.1799382894.1568007567; _gat=1; esi.Show=; esi.Type=; esi.FilterValue=; esi.GroupBy=; esi.FilterBy=; esi.authorsList=; esi.frontList=; esi.fieldsList=; esi.instList=; esi.journalList=; esi.terriList=; esi.titleList=
Host: fbzzde53972df5b34b0ca817704053506eebsx9v00ok5ou906n5q.faia.ncu.cwkeji.cn:8080
Referer: http://fbzzde53972df5b34b0ca817704053506eebsx9v00ok5ou906n5q.faia.ncu.cwkeji.cn:8080/IndicatorsAction.action?wsid=8DTjwndTYIpGUmtwDWS&Init=Yes&SrcApp=IC2LS&SID=J2-eF25I0yoGOb3hEK9ye2Ou8I5UOx2BFTYit-18x2dO7NdFIF5Q2oeA24DqhpckAx3Dx3DmSx2BPsTZLQCZ8x2BKZ8EWQEJAx3Dx3D-WwpRYkX4Gz8e7T4uNl5SUQx3Dx3D-wBEj1mx2B0mykql8H4kstFLwx3Dx3D
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
X-Requested-With: XMLHttpRequest'''.split("\n")
    headers = {i.split(":")[0]: i.split(":")[1].strip() for i in headers}

    # headers={'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Cookie': 'esi.isLocalStorageCleared=true; _ga=GA1.2.574408009.1567741924; _gid=GA1.2.1402796661.1567741924; esi.Show=; esi.Type=; esi.FilterValue=; esi.GroupBy=; esi.FilterBy=; esi.authorsList=; esi.frontList=; esi.fieldsList=; esi.instList=; esi.journalList=; esi.terriList=; esi.titleList=; esi.docsActiveTab=1; _sp_id.6486=fc5afcfc-eb13-47ae-8d07-18b426415d89.1567741812.2.1567765273.1567741832.facb4cf0-42e5-4c55-99bb-5d4996b6fd57; ezproxy=eM4AbFuHnrkd2RK; _gat=1', 'Host': 'esi-clarivate-com.ezproxy.cul.columbia.edu', 'Referer': ' https://esi-clarivate-com.ezproxy.cul.columbia.edu/IndicatorsAction.action?wsid=8C29CjIsgDIva5iGPh4&Init=Yes&SrcApp=IC2LS&SID=J3-x2B2Zl7re8x2FEMOWW77G6iuebYx2BhKjCaWdr-18x2dJxxEYgU6w81Ea4tn0JGiq6Ax3Dx3Do4UV45fV34hr5uugh9S8rgx3Dx3D-03Ff2gF3hTJGBPDScD1wSwx3Dx3D-cLUx2FoETAVeN3rTSMreq46gx3Dx3D', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36', 'X-Requested-With': 'XMLHttpRequest'}

    institution = []
    field = []
    #通过对象传递学校和领域
    #institution和field先处理好
    with open('china.txt','r') as f:
        res=f.readlines()
        for i in res:
            institution.append(i)

    with open('field.txt','r') as f1:
        res2=f1.readlines()
        for j in res2:
            field.append(j.upper())

    #增加时间戳来替换dc的内容
    stamp=int((time.time()+1)*1000)
    #原始url 需要增添 institution  field stamp参数
    for m in institution:
        for n in field:
            stamp=stamp+1
            url = Crawl(n.replace(' ','%20').replace(',','%2C').replace('/','%2').replace('&','%26').replace("'",'%27').replace('\n',''), m.replace(' ','%20').replace(',','%2C').replace('/','%2').replace('&','%26').replace("'",'%27').replace('\n',''),stamp)
            # print(url.get_information())
            urls=url.get_information()
            # print(urls)
            try:
                all = requests.get(url=urls, headers=headers)
                # print(all.json())
                if all.json():
                    content = all.json()
                    result = content['convertedData']
                    df = pd.DataFrame(result)

                    folder_path = "D:/spider_things/2019/" + m.replace('\n','') + "/"
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                        df.to_excel(folder_path + n.replace('\n', '') + ".xlsx")
                        print(folder_path + n.replace('\n', ''))
                    # if not folder_path + n.replace('\n','') + ".xlsx":
                    #     print(folder_path + n.replace('\n',''))
                    else:
                        df.to_excel(folder_path + n.replace('\n','') + ".xlsx")
                        print(folder_path + n.replace('\n', ''))
                else:
                    print('未获取到json:', i, j)

            except:
                print(n.replace('\n',''),m.replace('\n',''))
                with open('error.txt','a+') as f:
                    f.write(n.replace('\n','')+m.replace('\n',''))
