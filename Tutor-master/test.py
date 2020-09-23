import random
'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say(self, word):
        print(f'{self.name}说："{word}"')
        
zhang_san = Person('张三', '18', '男')
li_si = Person('李四', '20', '女')
zhang_san.say('你好')
li_si.say('你也好')
'''

resume = '''
         学生信息管理系统
    0.推出系统
    1.显示所有学生信息
    2.新建学生信息
    3.修改学生信息
    4.删除学生信息
    5.查询学生信息
    6.显示菜单
'''


def show_all():
    for student in data:
        print(student)


def create_new():
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    gender = input('请输入学生性别：')
    new_student = {'name': name,
                   'age': age,
                   'gender': gender}
    data.append(new_student)


def modify():
    name = input('请输入学生姓名：')
    for student in data:
        if student['name'] == name:
            print(student)
            student['name'] = input('请输入学生姓名（修改）：')
            student['age'] = int(input('请输入学生年龄（修改）：'))
            student['gender'] = input('请输入学生性别（修改）：')
            return
    else:
        print('查无此人')


def find_student():
    name = input('请输入学生姓名：')
    for student in data:
        if student['name'] == name:
            print(student)
            return
    else:
        print('查无此人')


def delete_student():
    name = input('请输入学生姓名：')
    for student in data:
        if student['name'] == name:
            print(student)
            data.remove(student)

            return
    else:
        print('查无此人')


data = [
    {'name': 'Billy',
     'age': 21,
     'gender': 'male'},
    {'name': 'Alice',
     'age': 22,
     'gender': 'female'},
]
print(resume)
while True:

    op = int(input('请输入数字：'))
    if op == 1:
        show_all()
    elif op == 2:
        create_new()
    elif op == 3:
        modify()
    elif op == 4:
        delete_student()
    elif op == 5:
        find_student()
    elif op == 6:
        print(resume)
    elif op == 0:
        break