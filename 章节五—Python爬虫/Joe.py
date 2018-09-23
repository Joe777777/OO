# -*-coding:utf-*

from urllib import request

if __name__ == '__main__':
    url = "http://quote.eastmoney.com/center/"

rsp = request.urlopen(url)
# 打开相应url并把相应页面作为返回

html = rsp.read()
print(type(html))
# 把返回结果读取出来
# 读取出来内容类型为bytes

html = html.decode()
# 如果想把bytes内容转换成字符串，需要解码

print(html)
