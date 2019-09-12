# -*- coding: utf-8 -*-
# 作者: xcl
# 时间: 2019/9/11 8:34


# 库

import pandas as pd
import os
# 路径

for modis in ['MOD2018', 'MYD2018']:
    input_file_path_pollution = "D:\\毕业论文程序\\NDVI\\DATA\\%s\\" % modis
    list1 = os.listdir(input_file_path_pollution)
    for file in list1:
        data = pd.read_excel(input_file_path_pollution+file, index_col ='日期')
        del data['监测站']
        data.to_excel(input_file_path_pollution+file)