import requests
import os
import re
import pandas as pd
import time
import random
suiji = random.random()*10

first = '<div id="menu_dl_panel_0" class="arch_panel zl_panel_selected"><div class="zl_item" id="archid_14635"><img class="zl_item_slt" src="images/indy/14635.png"><p class="zl_item_name">农林牧渔业</p></div><div class="zl_item" id="archid_16895"><img class="zl_item_slt" src="images/indy/16895.png"><p class="zl_item_name">农业</p></div><div class="zl_item" id="archid_17782"><img class="zl_item_slt" src="images/indy/17782.png"><p class="zl_item_name">林业</p></div><div class="zl_item" id="archid_17930"><img class="zl_item_slt" src="images/indy/17930.png"><p class="zl_item_name">畜牧业</p></div><div class="zl_item" id="archid_18262"><img class="zl_item_slt" src="images/indy/18262.png"><p class="zl_item_name">渔业</p></div><div class="zl_item" id="archid_18508"><img class="zl_item_slt" src="images/indy/18508.png"><p class="zl_item_name">农、林、牧、渔服务业</p></div></div>'
second='<div id="menu_dl_panel_1" class="arch_panel zl_panel_selected"><div class="zl_item" id="archid_1"><img class="zl_item_slt" src="images/indy/1.png"><p class="zl_item_name">建筑业</p></div><div class="zl_item" id="archid_201"><img class="zl_item_slt" src="images/indy/201.png"><p class="zl_item_name">房屋建筑业</p></div><div class="zl_item" id="archid_245"><img class="zl_item_slt" src="images/indy/245.png"><p class="zl_item_name">土木工程建筑业</p></div><div class="zl_item" id="archid_289"><img class="zl_item_slt" src="images/indy/289.png"><p class="zl_item_name">建筑安装业</p></div><div class="zl_item" id="archid_333"><img class="zl_item_slt" src="images/indy/333.png"><p class="zl_item_name">建筑装饰和其他建筑业</p></div><div class="zl_item" id="archid_377"><img class="zl_item_slt" src="images/indy/377.png"><p class="zl_item_name">工业</p></div><div class="zl_item" id="archid_573"><img class="zl_item_slt" src="images/indy/573.png"><p class="zl_item_name">采矿业</p></div><div class="zl_item" id="archid_769"><img class="zl_item_slt" src="images/indy/769.png"><p class="zl_item_name">煤炭开采和洗选业</p></div><div class="zl_item" id="archid_965"><img class="zl_item_slt" src="images/indy/965.png"><p class="zl_item_name">石油和天然气开采业</p></div><div class="zl_item" id="archid_1161"><img class="zl_item_slt" src="images/indy/1161.png"><p class="zl_item_name">黑色金属矿采选业</p></div><div class="zl_item" id="archid_1357"><img class="zl_item_slt" src="images/indy/1357.png"><p class="zl_item_name">有色金属矿采选业</p></div><div class="zl_item" id="archid_1553"><img class="zl_item_slt" src="images/indy/1553.png"><p class="zl_item_name">非金属矿采选业</p></div><div class="zl_item" id="archid_1749"><img class="zl_item_slt" src="images/indy/1749.png"><p class="zl_item_name">其他采矿业</p></div><div class="zl_item" id="archid_1945"><img class="zl_item_slt" src="images/indy/1945.png"><p class="zl_item_name">开采辅助活动</p></div><div class="zl_item" id="archid_2141"><img class="zl_item_slt" src="images/indy/2141.png"><p class="zl_item_name">制造业</p></div><div class="zl_item" id="archid_2337"><img class="zl_item_slt" src="images/indy/2337.png"><p class="zl_item_name">农副食品加工业</p></div><div class="zl_item" id="archid_2533"><img class="zl_item_slt" src="images/indy/2533.png"><p class="zl_item_name">食品制造业</p></div><div class="zl_item" id="archid_2729"><img class="zl_item_slt" src="images/indy/2729.png"><p class="zl_item_name">酒、饮料和精制茶制造业</p></div><div class="zl_item" id="archid_2925"><img class="zl_item_slt" src="images/indy/2925.png"><p class="zl_item_name">烟草制品业</p></div><div class="zl_item" id="archid_3121"><img class="zl_item_slt" src="images/indy/3121.png"><p class="zl_item_name">纺织业</p></div><div class="zl_item" id="archid_3317"><img class="zl_item_slt" src="images/indy/3317.png"><p class="zl_item_name">纺织服装、服饰业</p></div><div class="zl_item" id="archid_3513"><img class="zl_item_slt" src="images/indy/3513.png"><p class="zl_item_name">皮革、毛皮、羽毛及其制品和制鞋业</p></div><div class="zl_item" id="archid_3709"><img class="zl_item_slt" src="images/indy/3709.png"><p class="zl_item_name">木材加工和木、竹、藤、棕、草制品业</p></div><div class="zl_item" id="archid_3905"><img class="zl_item_slt" src="images/indy/3905.png"><p class="zl_item_name">家具制造业</p></div><div class="zl_item" id="archid_4101"><img class="zl_item_slt" src="images/indy/4101.png"><p class="zl_item_name">造纸和纸制品业</p></div><div class="zl_item" id="archid_4297"><img class="zl_item_slt" src="images/indy/4297.png"><p class="zl_item_name">印刷和记录媒介复制业</p></div><div class="zl_item" id="archid_4493"><img class="zl_item_slt" src="images/indy/4493.png"><p class="zl_item_name">文教、工美、体育和娱乐用品制造业</p></div><div class="zl_item" id="archid_4689"><img class="zl_item_slt" src="images/indy/4689.png"><p class="zl_item_name">石油加工、炼焦和核燃料加工业</p></div><div class="zl_item" id="archid_4885"><img class="zl_item_slt" src="images/indy/4885.png"><p class="zl_item_name">化学原料和化学制品制造业</p></div><div class="zl_item" id="archid_5081"><img class="zl_item_slt" src="images/indy/5081.png"><p class="zl_item_name">医药制造业</p></div><div class="zl_item" id="archid_5277"><img class="zl_item_slt" src="images/indy/5277.png"><p class="zl_item_name">化学纤维制造业</p></div><div class="zl_item" id="archid_5473"><img class="zl_item_slt" src="images/indy/5473.png"><p class="zl_item_name">非金属矿物制品业</p></div><div class="zl_item" id="archid_5669"><img class="zl_item_slt" src="images/indy/5669.png"><p class="zl_item_name">黑色金属冶炼和压延加工业</p></div><div class="zl_item" id="archid_5865"><img class="zl_item_slt" src="images/indy/5865.png"><p class="zl_item_name">有色金属冶炼和压延加工业</p></div><div class="zl_item" id="archid_6061"><img class="zl_item_slt" src="images/indy/6061.png"><p class="zl_item_name">金属制品业</p></div><div class="zl_item" id="archid_6257"><img class="zl_item_slt" src="images/indy/6257.png"><p class="zl_item_name">通用设备制造业</p></div><div class="zl_item" id="archid_6453"><img class="zl_item_slt" src="images/indy/6453.png"><p class="zl_item_name">专用设备制造业</p></div><div class="zl_item" id="archid_6649"><img class="zl_item_slt" src="images/indy/6649.png"><p class="zl_item_name">电气机械和器材制造业</p></div><div class="zl_item" id="archid_6845"><img class="zl_item_slt" src="images/indy/6845.png"><p class="zl_item_name">计算机、通信和其他电子设备制造业</p></div><div class="zl_item" id="archid_7041"><img class="zl_item_slt" src="images/indy/7041.png"><p class="zl_item_name">仪器仪表制造业</p></div><div class="zl_item" id="archid_7237"><img class="zl_item_slt" src="images/indy/7237.png"><p class="zl_item_name">其他制造业</p></div><div class="zl_item" id="archid_7433"><img class="zl_item_slt" src="images/indy/7433.png"><p class="zl_item_name">废弃资源综合利用业</p></div><div class="zl_item" id="archid_7629"><img class="zl_item_slt" src="images/indy/7629.png"><p class="zl_item_name">橡胶和塑料制品业</p></div><div class="zl_item" id="archid_7825"><img class="zl_item_slt" src="images/indy/7825.png"><p class="zl_item_name">汽车制造业</p></div><div class="zl_item" id="archid_8021"><img class="zl_item_slt" src="images/indy/8021.png"><p class="zl_item_name">铁路船舶航空航天其他运输设备制造业</p></div><div class="zl_item" id="archid_8217"><img class="zl_item_slt" src="images/indy/8217.png"><p class="zl_item_name">金属制品、机械和设备修理业</p></div><div class="zl_item" id="archid_8413"><img class="zl_item_slt" src="images/indy/8413.png"><p class="zl_item_name">电力、热力、燃气及水生产和供应业</p></div><div class="zl_item" id="archid_8609"><img class="zl_item_slt" src="images/indy/8609.png"><p class="zl_item_name">电力、热力生产和供应业</p></div><div class="zl_item" id="archid_8805"><img class="zl_item_slt" src="images/indy/8805.png"><p class="zl_item_name">燃气生产和供应业</p></div><div class="zl_item" id="archid_9001"><img class="zl_item_slt" src="images/indy/9001.png"><p class="zl_item_name">水的生产和供应业</p></div></div>'
third='<div id="menu_dl_panel_2" class="arch_panel zl_panel_selected"><div class="zl_item" id="archid_18552"><img class="zl_item_slt" src="images/indy/18552.png"><p class="zl_item_name">房地产</p></div><div class="zl_item" id="archid_19827"><img class="zl_item_slt" src="images/indy/19827.png"><p class="zl_item_name">交通运输、仓储和邮政业</p></div><div class="zl_item" id="archid_20792"><img class="zl_item_slt" src="images/indy/20792.png"><p class="zl_item_name">金融业</p></div><div class="zl_item" id="archid_22178"><img class="zl_item_slt" src="images/indy/22178.png"><p class="zl_item_name">批发和零售业</p></div><div class="zl_item" id="archid_24204"><img class="zl_item_slt" src="images/indy/24204.png"><p class="zl_item_name">住宿和餐饮业</p></div><div class="zl_item" id="archid_23759"><img class="zl_item_slt" src="images/indy/23759.png"><p class="zl_item_name">信息传输、软件和信息技术服务业</p></div><div class="zl_item" id="archid_25720"><img class="zl_item_slt" src="images/indy/25720.png"><p class="zl_item_name">科学研究和技术服务业</p></div><div class="zl_item zl_item_more"><img class="zl_item_slt" src="images/indy/0.png"><p class="zl_item_name">更多行业数据陆续更新中...</p></div></div>'
ui='<div id="menu_dl_panel_3" class="arch_panel zl_panel_selected"><div class="zl_item" id="archid_53950"><img class="zl_item_slt" src="images/indy/53950.png"><p class="zl_item_name">电子</p></div><div class="zl_item" id="archid_54521"><img class="zl_item_slt" src="images/indy/54521.png"><p class="zl_item_name">机械</p></div><div class="zl_item" id="archid_55540"><img class="zl_item_slt" src="images/indy/55540.png"><p class="zl_item_name">建材</p></div><div class="zl_item" id="archid_55846"><img class="zl_item_slt" src="images/indy/55846.png"><p class="zl_item_name">旅游</p></div><div class="zl_item" id="archid_56673"><img class="zl_item_slt" src="images/indy/56673.png"><p class="zl_item_name">轻工</p></div><div class="zl_item" id="archid_57016"><img class="zl_item_slt" src="images/indy/57016.png"><p class="zl_item_name">商贸</p></div><div class="zl_item" id="archid_60083"><img class="zl_item_slt" src="images/indy/60083.png"><p class="zl_item_name">石化</p></div><div class="zl_item" id="archid_60559"><img class="zl_item_slt" src="images/indy/60559.png"><p class="zl_item_name">冶金</p></div><div class="zl_item zl_item_more"><img class="zl_item_slt" src="images/indy/0.png"><p class="zl_item_name">更多行业数据陆续更新中...</p></div></div>'

yi = re.findall('<img class="zl_item_slt" src="images/indy/(\d+).png"><p class="zl_item_name">(.*?)</p>',first)
er=re.findall('<img class="zl_item_slt" src="images/indy/(\d+).png"><p class="zl_item_name">(.*?)</p>',second)
san=re.findall('<img class="zl_item_slt" src="images/indy/(\d+).png"><p class="zl_item_name">(.*?)</p>',third)[:-1]
uic=re.findall('<img class="zl_item_slt" src="images/indy/(\d+).png"><p class="zl_item_name">(.*?)</p>',ui)[:-1]
for ind in uic:
    indco = ind[0]
    ind=ind[1]
    ind_name = '\\'+ ind[1]
    # print(indco,ind)


    headers = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: ASP.NET_SessionId=ggeegnlcchzn0athwieositc; ASPSESSIONIDSQRDDQRS=DJINJIEDMOLNOJCNABHAKECN; zb=22821
Host: mcin.macrochina.cn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'''.split('\n')

    headers = {i.split(":")[0]:i.split(":")[1].strip() for i in headers}
    time.sleep(suiji)
    response = requests.post(headers = headers,url='http://mcin.macrochina.cn/api/GetArchAnsyJson?id={0}'.format(indco))
    # response = requests.post(headers=headers, url='http://mcin.macrochina.cn/api/GetArchAnsyJson?id=14635')

    result = response.json()
    '''
    ['frontArchItem']['showname']上游
    ['afterArchItem']['showname']下游
    
    '''
    try:
        if result['frontArchItem']:
            for i in result['frontArchItem']:

                print(ind,'上游：',i['showname'])
        else:
            print(ind,indco,'没有上游')
        if result['afterArchItem']:
            for j in result['afterArchItem']:
                print(ind,'下游：',j['showname'])
        else:
            print(ind,indco,'没有下游')
    except:
        print(indco,ind)
    # front=result['frontArchItem']['showname']
    # after=result['afterArchItem']['showname']

    # print(front,after)
