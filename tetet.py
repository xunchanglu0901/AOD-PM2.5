# -*- coding: utf-8 -*-
# 作者: xcl
# 时间: 2019/8/7 11:10


# 库
from multiprocessing import Process  # 多线程,提高CPU利用率
import copy
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import os

# 思路
# K循环 插补 去 参数b

x = 16/3

stc = x**3 - 8*x**2 + 22*x + 90
tr = x * 22
print(stc-tr)