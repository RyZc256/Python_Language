#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: oopDemo
# @ File: my_pickle
# @ Time: 24/4/2023 上午8:29
# @ Author: hz157
# @ Github: https://github.com/hz157
import os
import pickle

from proj.config.settings import *


class MyPickle:

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, 'ab') as fp:
            pickle.dump(data, fp)

    def readier(self):
        with open(self.filename, 'rb') as fp:
            while True:
                try:
                    data = pickle.load(fp)
                    yield data
                except:
                    break

    def delete(self, name):
        fp = MyPickle(self.filename+".bak")
        for item in self.readier():
            if item.name == name:
                pass
            else:
                fp.write(item)
        os.remove(self.filename)
        os.rename(self.filename + ".bak", self.filename)