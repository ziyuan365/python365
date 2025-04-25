print("###################")
print("OOP_demo_01:")
#封装
#创建一个类并把它实例化
class Student:
#学生类
    def __init__(self,name,age,gender):
        #类的初始化
        self.name=name
        self.age=age
        self.gender=gender
    def eat(self):
        #定义类函数
        print("{0},{1}岁，{2},吃饭".format(self.name,self.age,self.gender))
    def drink(self):
        print("{0},{1}岁，{2},喝水".format(self.name,self.age,self.gender))
    def sleep(self):
        print("{0},{1}岁，{2},睡觉".format(self.name,self.age,self.gender))
person1=Student('Jack',18,'男')#实例化对象
#调用类方法
person1.eat()
person1.drink()
person1.sleep()
person2=Student('sue',19,'女')
person2.eat()
person2.drink()
person2.sleep()



print("###################")
print("OOP_demo_02")
#继承
class Animal:
    def __init__(self):
        #设置name的值为空
        self.name=None
    def eat(self):
            print("{0}在吃饭".format(self.name))
    def drink(self):
            print("{0}在喝水".format(self.name))
    def sleep(self):
            print("{0}在睡觉".format(self.name))
#创建猫类，继承动物类
class Cat(Animal):
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    def introduce(self):
        print("小猫的名字是{0}，年龄是{1}".format(self.name,self.age))
    def catch_mouse(self):
        print("小猫{0}在抓老鼠".format(self.name,))
    def jump(self):
        print("小猫{0}在跳高".format(self.name))
#定义狗类，继承动物类
class  Dog(Animal):
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    def introduce(self):
            print("小狗的名字是{0}，他今年{1}岁了".format(self.name,self.age))
    def guard(self):
            print("小狗{0}在看门".format(self.name))
    def swimming(self):
            print("小狗{0}在游泳".format(self.name))
cat=Cat('小花',7)       #创建一个cat对象，以后调用对象
cat.introduce()
cat.drink()
cat.sleep()
cat.catch_mouse()
cat.jump()
dog=Dog('旺财',10)
dog.introduce()
dog.drink()
dog.eat()
dog.sleep()
dog.guard()
dog.swimming()



print("###################")
print("OOP_demo_03:")
#多态
print("python语言本来就是多态语言")



print("###################")
print("OOP_demo_04:")
class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def introduce(self):
        print("我的名字是{0}，年龄是{1}，学号是{2}".format(self.name,self.age,self.id))
    def say_school(self):
        print("我来自XX学校")
#实例化对象
s1=Student('小华',18,'2023240001')
s1.introduce()
s1.say_school()
s2=Student('小李',19,'1234567890')
s2.introduce()
s2.say_school()



print("###################")
print("OOP_demo_05:")
#类的使用
#定义一个book类并定义属性，然后将类实例化、
class Book:
     #定义类属性
     author=""
     name=""
     pages=""
     price=""
     press=""
#实例化book类
my_book1=Book()
print(my_book1)
#访问类属性
print(my_book1.author)
print(my_book1.pages)
print(my_book1.price)
#设置类属性
my_book1.author="jack"
my_book1.pages=350
my_book1.price=35
#重新访问类属性
print(my_book1.author)
print(my_book1.pages)
print(my_book1.price)
my_book2=Book()
print(my_book2.author)
print(my_book2.pages)
print(my_book2.price)
my_book2.author="Sue"
my_book2.pages=350
my_book2.price=35
print(my_book2.author)
print(my_book2.pages)
print(my_book2.price)



print("###################")
print("OOP_demo_06:")
#类属性被覆盖，实例的输出发生改变
class A:
     name="A"
     num=2
print(A.name)
print(A.num)
a=A()
print(a.name)
print(a.num)
b=A()
print(b.name)
print(b.num)
A.name="B"
print(a.name)
print(b.name)



print("###################")
print("OOP_demo_07:")
#错误示范，静态变量会将eat（）没有了类的属性（将其截取）
# class Person(object):
#     def __init__(self,name):
#           self.name=name
#     @staticmethod  把eat方法变为静态方法
#     def eat(self):
#          print("%s is eating" % self.name)
# d=Person("xiaoming")
# d.eat()
#正确示范
class Person(object):
    def __init__(self,name):
          self.name=name
    @staticmethod
    def eat(x):
         print("{0} is eating" .format(x))
# d=str="xiaoming"
d=Person('xiaoming')
d.eat("jack")       #将eat（）当作一个独立的函数传参给他



print("###################")
print("OOP_demo_08:")
#类方法 @classmethond方法
#错误演示
# class Person(object):
#      def __init__(self,name):
#           self.name=name
#      @classmethod
#      def eat(self):
#           print("%s is eating"%self.name)
# d=Person("小明")
# d.eat()
#正确示范
class Person(object):
     name="Jack"
     def __init__(self,name):
          self.name=name
     @classmethod
     def eat(self):
          print("%s is eating"%self.name)       #访问类属性并返回
d=Person("小明")
d.eat()



print("###################")
print("OOP_demo_09:")
#属性方法
#错误示范
# class Person(object):
#      def __init__(self,name):
#           self.name=name
#      @property      #将eat（）变成属性，不再是方法
#      def eat(self):
#           print("%s in eating"%self.name)
# d=Person("xiaoming")
# d.eat()
# 正确示范
class Person(object):
     def __init__(self,name):
          self.name=name
     @property      #将eat（）变成属性，不再是方法
     def eat(self):
          print("%s in eating"%self.name)
d=Person("xiaoming")
d.eat        #调用属性直接调用，不用加括号



print("###################")
print("OOP_demo_10:")
#私有成员与公有成员
class a:
     def __init__(self):
        self.num1=123
        self.__num2=456
class b(a):
     def __init__(self,name):
        self.name=name
        self.__age=18
        super(b,self).__init__()#这一行不报错
#定义类方法
     def show(self):
          print(self.name)
          print(self.__age)#在类里面调用私有变量
          print(self.num1)#调用b类中继承的父类（a）的属性
        #   print(self.__num2)#父类中的私有变量不会被子类继承
obj=b("小明")#将b类实例化为obj
print(obj.name)#调用b类中的name属性
print(obj.num1)#调用a类中的num1（被b类继承）属性
obj.show ()



print("###################")
print("OOP_add()_demo_11:")
class abc:
     def __init__(self,age):
        self.age=age
     def __add__(self,obj):
          return self.age+obj.age
a1=abc(18)
a2=abc(20)
print(a1+a2)



print("###################")
print("OOP_dict()_demo_12:")
#列举出类或对象中的所有成员
class abc:
     def __init__(self,age):
        self.age=age
     def __add__(self,obj):
          return self.age+obj.age
a1=abc(18)
print(abc.__dict__)#列举类的成员
print(a1.__dict__)#列举对象的成员



print("###################")
print("OOP_getitem()_setitem()_delitem()_demo_13:")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __getitem__(self,item):#匹配：对象[item]这中形式
         return item+10
    def __setitem__(self,key,value):#匹配：对象[key]=value这种形式
         print(key,value)
    def __delitem__(self,key):#匹配：del对象[key]这种形式
         print(key) 
#实例化类
li=Person("Alex",18)
print(li[10])
li[10]=100
del li[10]



print("###################")
print("OOP_getslice()_setslice()_delslice()_demo_14:")
class Foo:
    def __init__(self,name ,age):
        self.name=name
        self.age=age
        self.li=[1,2,3,4,5,6,7]
    def __getitem__(self,item):
         if isinstance(item,slice):
              return self.li[item]
         elif isinstance(item,int):
              return item+10
    def __setitem__(self,key,value):
         print(key,value)
    def __delitem__(self,key):
         print(key)
    def __getslice__(self,index1,index2):
         print(index1,index2)
li=Foo("Alice",18)
print(li[3:5])



print("###################")
print("OOP_iter()_demo_15:")
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __iter__(self):
         return iter([1,2,3,4,5])
li=Foo("Alex",18)
'''
1.如果类中有__iter__()方法，它的对象就是可迭代对象
2.对象__iter()的返回值就是一个迭代器
3.for循环如果是迭代器,直接执行__next__()方法
4.for循环如果是可迭代对象,先执行__iter__()方法,获取迭代器再执行__next__()方法
'''    
for i in li:
     print(i)



print("###################")
print("OOP_isinstance()_demo_16:")
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Son(Foo):
     pass
obj=Son("xiaoming",18)
print(isinstance(obj,Foo))#判断obj是否是Foo的对象



print("###################")
print("OOP_issubclass()_demo_17:")
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Son(Foo):
     pass
obj=Son("xiaoming",18)
print(issubclass(Son,Foo))#判断obj是否是Foo的对象



print("###################")
print("OOP_new()_metaclass()_demo_18:")
#类实例化对象内部的实现过程
class Mytype(type):
    #初始化类
    def __init__(self,what,bases=None,dict=None):
    #继承类
        super(Mytype,self).__init__(what,bases,dict)
    #定义类方法
    def __call__(self, *args, **kwds):
    #设置类属性
        obj=self.__new__(self)
        self.__init__(obj,*args, **kwds)
        return obj
#创建类
class Foo:
     #定义类属性
    class Foo(metaclass=Mytype):  # 新语法
        pass
     #初始化类
    def __init__(self,name,age):
          self.name=name
          self.age=age
    def __new__(cls,*args, **kwds):#创建对象实例：分配内存并创建对象实例
          return object.__new__(cls)#cls：当前类（不是实例），由 Python 自动传入。*args, **kwds：传递给 __new__ 的参数，通常原样传递给 __init__。
#实例化类
obj=Foo("xiaoming",18)
print(obj.name,obj.age)
 


print("###################")
print("OOP_try_demo_19:")
try:
     int("aaa")
except IndexError as e:
    '''
    捕捉索引异常的子异常
    '''
    print("IndexError:",e)
except ValueError as e:
    print("ValueError",e)
except Exception as e:
    '''
如果上面两个异常没有捕获,那么使用Exception捕获,Excption能够捕获所有的异常
    '''
    print("Exception:",e)
else:
     print("True")
finally:
     '''
     不管是否发生异常,最后都会执行finally代码,加入try里面的代码正常执行,则先执行else中的代码,在执行finally中的代码。
     '''
     print("finally")