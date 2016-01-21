# -*- coding: utf-8 -*-
import requests, sys
import re    # ������ʽ
from bs4 import BeautifulSoup    #������ҳHTML

# ��ȡ����ҳ���Դ����
def getHtml(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception('HTTP request error: %d' % resp.status_code)
    return resp.text

# ��ȡ�Ͻ�������
#sseHtml = getHtml("http://2016.sse.com.cn/disclosure/listedinfo/announcement/")
#print(html)
jcHtml = getHtml("http://www.cninfo.com.cn/cninfo-new/index/")

parsedHtml = BeautifulSoup(jcHtml, 'html.parser')
announcements = parsedHtml.find(id = 'con-a-1').find_all('li')
for item in announcements:
    # class=t1��Ӧ����, class=t2��Ӧ����
    print item.find(class_ = 't1').text, item.find(class_ = 't2').text
    # class=t3 or t4��Ӧ�������
    print ','.join(map(lambda item: item['title'] if item.get('title') != None else item.text.strip(), item.find_all('a')))
