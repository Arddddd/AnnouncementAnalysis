# -*- coding: utf-8 -*-
import urllib.request as ur
import re    # ������ʽ


# ��ȡ����ҳ���Դ����
def getHtml(url):
    request = ur.Request(url)
    response = ur.urlopen(request)
    html = response.read()
    return html


# ��ȡ��ҳԴ�����е�ĳ����Դ�б�
def getTitle(html):
    html = html.decode('utf-8')
    # pattern = re.compile(r'title="(.*?)"')    # ��̰���ֲ�ƥ��title
    #pattern = re.compile(r'target="_blank">(.+?)</a>')
    pattern = re.compile(r'<li>(.+?)</li>')
    titles = re.findall(pattern, html)
    return list(set(titles))


# ��ȡ�Ͻ�������
#sseHtml = getHtml("http://2016.sse.com.cn/disclosure/listedinfo/announcement/")
#print(html)
jcHtml = getHtml("http://www.cninfo.com.cn/cninfo-new/index/")
# ��ȡ��������б�
jcTitle = getTitle(jcHtml)


print(jcTitle)