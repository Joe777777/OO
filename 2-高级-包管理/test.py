# -*-coding:utf-*
# class DanaValueError(ValueError):
pass

try:
    print("我爱王晓静")
    print(3.1415926)
    # 手动引发一个异常
    #  注意语法：raise ErrorClassName
    raise ValueError
    print("还没完呀")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我一定会被执行")