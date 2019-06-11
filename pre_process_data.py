# -*- coding:utf-8 -*-
# Imports

# Numpy,Pandas
import numpy as np
import pandas as pd

# matplotlib,seaborn,pyecharts

import matplotlib.pyplot as plt
plt.style.use('ggplot')  #风格设置近似R这种的ggplot库
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline
import missingno as msno

#  忽略弹出的warnings
import warnings
warnings.filterwarnings('ignore')  

pd.set_option('display.float_format', lambda x: '%.5f' % x)
