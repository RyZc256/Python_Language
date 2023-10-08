#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: start
# @ Time: 24/4/2023 上午8:28
# @ Author: hz157
# @ Github: https://github.com/hz157

import os, sys

from proj.src import main

BASE_PATH = os.path.dirname(os.getcwd())
sys.path.insert(0, BASE_PATH)


if __name__ == '__main__':
    main.main()
