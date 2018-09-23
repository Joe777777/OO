# -*-coding:utf-*

'''
利用request下载页面，自动检测页面编码
'''

from urllib import request
import chardet

if __name__ == '__main__':
    url = 'http://finance.eastmoney.com/news/1345,20180923951189228.html'

    rsp = request.urlopen(url)

    html = rsp.read()

    # 利用 chardet自动检测编码
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)