# -*-coding:utf-*

# 利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
# 导入多线程包并更名为thread

import threading

def loop1(int1):
    # ctime 得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 把参数打印出来
    print("我是参数", int1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2(int1, int2):
    # ctime 得到当前时间
    print("Start loop2 at:", time.ctime())
    # 把参数打印出来
    print("我是参数", int1, "和参数", int2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("xiaoming",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("zhangsan", "lisi"))
    t2.start()

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)