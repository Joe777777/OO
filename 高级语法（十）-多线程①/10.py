# -*-coding:utf-*

import threading
from time import sleep,ctime

loop = [4,2]

class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        '''
        :param nloop: loop函数名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print("Start loop ", nloop, "at", ctime())
        sleep(nsec)
        print("Done loop ", nloop, "at", ctime())

def main():
        print("Starting at: ", ctime())

        # ThreadFunc("loop").loop 跟以下两个式子相等：
        # t = ThreadFunc("loop")
        # t.loop
        # 以下t1 和 t2 的定义方式相等
        t = ThreadFunc("loop")
        t1 = threading.Thread(target=t.loop, args=("Loop1", 4))
        # 下面这张写法更西方一些，工业化一点
        t2 = threading.Thread(target=ThreadFunc("loop").loop, args=("Loop2", 2))

        # 常见错误写法
        # t1 = threading.Thread(target=ThreadFunc("loop").loop(100,4))
        # t2 = threading.Thread(target=ThreadFunc("loop").loop(100,4))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("All done at: ", ctime())

if __name__ == '__main__':
    main()