# -*-coding:utf-*

import threading

sum = 0
loopSum = 100000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == '__main__':

# 常规运行方式，分别运行，分别得到各自结果
#    myAdd()
#    print(sum)
#    myMinu()
#    print(sum)

# 改成多线程
    print("Starting....{0}".format(sum))

# 开始多线程实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done....{0}".format(sum))

