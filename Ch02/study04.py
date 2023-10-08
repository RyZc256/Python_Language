# Copyright (c) 2023.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Project: Python
# @FileName: 2023_02_13/ch02/study04.py
# @Author：hz157    (https://github.com/hz157)
# @DateTime: 13/2/2023 上午11:01
import math


def main():
    print('请输入位正整数，以空格间隔')
    num = list(map(int, input().split(' ')))
    if num[0] + num[1] <= num[2] or num[2] + num[1] <= num[0] or num[2] + num[0] <= num[1]:
        print("该数值不能构成三角形")
        return None
    perimeter = num[0] + num[1] + num[2]
    p = 0.5 * perimeter
    area = math.sqrt(p * (p - num[0]) * (p - num[1]) * (p - num[2]))
    print(f'三角形的面积是{area}')
    print(f'三角形的周长是{perimeter}')


if __name__ == '__main__':
    main()
