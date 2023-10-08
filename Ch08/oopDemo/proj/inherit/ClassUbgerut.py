#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: ClassUbgerut
# @ Time: 24/4/2023 上午9:05
# @ Author: hz157
# @ Github: https://github.com/hz157

class SchoolMember(object):
    menber = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        print("[%s]注册成为学校的新成员！" % self.name)
        SchoolMember.menber += 1

    def tell(self):
        print('————————————%s—————————————' % self.name)
        for key, value in self.__dict__.items():
            print(key, value)
        print('————————————结束—————————————')

    def __del__(self):
        print("开除了[%s]" % self.name)
        SchoolMember.menber -= 1


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print("教师[%s] 正在教学[%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print("学生[%s] 花费了[%s]" % (self.name, self.amount))
        self.amount += amount


def main():
    teac1 = Teacher("张三", 28, 'M', 5860, "JAVA")
    teac1.tell()
    stu1 = Student("李四", 21, 'F', "JAVA", 9600)
    stu1.tell()
    stu2 = Student("王五", 20, 'M', "JAVA", 9600)
    print(SchoolMember.menber)
    del stu2
    print(SchoolMember.menber)


if __name__ == '__main__':
    main()
