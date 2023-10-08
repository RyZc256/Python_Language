#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: ClassPolymiorph
# @ Time: 24/4/2023 上午9:17
# @ Author: hz157
# @ Github: https://github.com/hz157
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a person, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, gender, course):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


def who_am_i(x):
    print(x.whoAmI())


def main():
    per = Person('张三', 'Male')
    teac1 = Teacher('李四', 'FeMale', 'BigData')
    stu1 = Student('王五', 'Male', 85)
    who_am_i(per)
    who_am_i(teac1)
    who_am_i(stu1)


if __name__ == '__main__':
    main()
