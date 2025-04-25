class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    
    # 访问器方法 (getters)
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone
    
    # 赋值器方法 (setters)
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone(self, phone):
        self.__phone = phone
    
    # 显示信息方法
    def display_info(self):
        print(f"姓名: {self.__name}")
        print(f"地址: {self.__address}")
        print(f"年龄: {self.__age}")
        print(f"电话: {self.__phone}")
        print("-" * 30)

# 创建三个实例
# 1. 自己的信息
myself = Person("张三", "北京市海淀区", 25, "13800138000")

# 2. 朋友的信息
friend = Person("李四", "上海市浦东新区", 28, "13900139000")

# 3. 家人的信息
family = Person("王五", "广州市天河区", 45, "13700137000")

# 显示信息
print("我的信息:")
myself.display_info()

print("朋友的信息:")
friend.display_info()

print("家人的信息:")
family.display_info()

# 示例修改信息
myself.set_address("深圳市南山区")
myself.set_phone("13600136000")
print("\n修改后的我的信息:")
myself.display_info()