class foo(object):

    def __int__(self, name):
        self.name = name

    def __str__(self):
        return self.name


obj1= foo("it部门")
print(obj1)  # 输出一个对象时，如果想要定制显示的内容。


obj2= foo("销售部")
print(obj2)  # 输出一个对象时，如果想要定制显示的内容。
