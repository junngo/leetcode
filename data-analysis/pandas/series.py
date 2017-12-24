import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3,6,9,12])

print(obj.values)
print(obj.index)

# casualties price
cas = Series([870000, 430000, 300000, 210000, 400000], index=['USSR', 'Germany', 'China', 'Japan', 'USA'])
print(cas)
print(cas['USA'])
