# -*-coding:utf-*

from urllib import request, parse
import chardet

'''
掌握对rul进行参数编码的方法，需要使用parse模块
'''

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input("Input your keyword:")

    # 要想使用data，需要使用字典结构
    qs = {
        "wd": wd
    }

    # 转换url编码
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)
    print(type(rsp))
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    html = rsp.read()

    # 利用 chardet自动检测编码
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)