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

# check witch countries had cas greater than 4 mill
print(cas[cas > 400000])

# check if a index or value as in a series
print('USSR' in cas)

# into dictionary
cas_dict = cas.to_dict()
print(cas_dict)

cas2 = Series(cas_dict)

countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
obj2 = Series(cas_dict, index=countries)
print(obj2, 'obj2')

print(pd.isnull(obj2))
print(pd.notnull(obj2))

print(cas2+obj2)

# you can give name series
obj2.name = "Casualties"
obj2.index.name = 'Countries'
