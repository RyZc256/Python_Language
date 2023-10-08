#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: main
# @ Time: 24/4/2023 上午8:29
# @ Author: hz157
# @ Github: https://github.com/hz157
from proj.src.manager import Manager


def main():
    mana = Manager.info
    for x in range(len(mana)):
        print(x+1, mana[x][0])
    while True:
        ch = input("请输入序号：").strip()
        getattr(Manager(), mana[int(ch)-1][1])()