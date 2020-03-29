#coding=utf-8
class HelloWorld:
    def __init__(self):
        self.name='chengjingjing'

    def sayHello(self):


        return "hello!!"


    def sayNihao(self):
        a=self.sayHello()
        return "你好！！",a

    def sayGood(self,url,name):
        return ""


if __name__ == '__main__':
    for i in range(1,10):
        print(i)