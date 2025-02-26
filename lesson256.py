import pandas as pd
import numpy as np

idx = pd.Index([10,20,30])
print(idx)

idx = pd.Index([1, 3.14])
print(idx)

idx = pd.Index(['element 1', 'element 2'])
print(idx)

idx = pd.Index([2,4,6,8,10])
print(idx)
print(idx[0])
print(idx[1:4])
print(idx[::-1])
print(idx[[1,3,4]])


