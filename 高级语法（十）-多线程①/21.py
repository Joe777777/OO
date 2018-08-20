# -*-coding:utf-*

import multiprocessing
import os

def info(tittle):
    print(tittle)
    print("module name:", __name__)
    # 得到父进程的id
    print("parent process:", os.getppid())
    # 得到本身进程的id
    print("process id:", os.getpid())

def f(name):
    info("function f")
    print("hello", name)

if __name__ == '__main__':
    info("main line")
    p = multiprocessing.Process(target=f, args=("bob",))
    p.start()
    p.join()