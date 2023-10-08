#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: manager
# @ Time: 24/4/2023 上午8:29
# @ Author: hz157
# @ Github: https://github.com/hz157
from proj.config.settings import *
from proj.src.my_pickle import MyPickle
from proj.src.teacher import Teacher


class Manager:
    info = [('查看教师', 'show_teacher'),
            ('创建教师', 'create_teacher'),
            ('删除教师', 'delete_teacher'),
            ('退出', 'exit')]

    def __init__(self):
        self.teacher_pickle_obj = MyPickle(teacher_file)

    def show(self, pickle_obj):
        pickle_obj = getattr(self, pickle_obj)
        data_info = pickle_obj.readier()
        for teacher_obj in data_info:
            for key in teacher_obj.__dict__:
                print(key, teacher_obj.__dict__[key])
            print('-' * 50)

    def show_teacher(self):
        print('教师信息'.center(45, '-'))
        self.show('teacher_pickle_obj')

    def create_teacher(self):
        name = input("请输入教师姓名: ").strip()
        eduname = input("请输入教师所在学校名称: ").strip()
        teacher = Teacher(name, eduname)
        self.teacher_pickle_obj.write(teacher)
        print('教师创建成功!')

    def delete_teacher(self):
        self.show_teacher()
        teachername = input("请输入要删除的教师姓名: ").strip()
        self.teacher_pickle_obj.delete(teachername)
        print('教师删除成功!')

    def exit(self):
        exit()
