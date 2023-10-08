#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: Student
# @ Time: 24/4/2023 上午8:30
# @ Author: hz157
# @ Github: https://github.com/hz157


class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    def print_info(self):
        return self.name + "  " + str(self.age) + "  " + str(self.count)


def main():
    s1 = Student("tom", 20)
    s2 = Student("rose", 19)
    s3 = Student("davi", 19)
    s4 = Student("lucy", 19)
    print("学生个数: {}".format(Student.count))


if __name__ == '__main__':
    main()
