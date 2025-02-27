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
print('-'*80)

idx = pd.Index(['London', 'Paris', 'New York', 'Tokyo'])
print(idx)
print(idx[idx != 'Tokyo'])
print(idx != 'Tokyo')
print('-'*80)

try:
    idx[0] = 100
except TypeError as ex:
    print('TypeError:',ex)

print(idx[0])
print(idx[1])
print('-'*80)

idx_1 = pd.Index(['a','b','c'])
idx_2 = pd.Index(['c','d','e'])
print(idx_1)
print(idx_2)
#print(idx_1 & idx_2)
#print(idx_1 | idx_2)
print(idx_1.intersection(idx_2))
print(idx_1.union(idx_2))
print('-'*80)

print(pd.Index([1,2,3]).union(pd.Index([0.1,0.2])))
print('-'*80)

print(pd.Index(range(2,10,2)))
print(pd.Index([2,4,6,8]))
print(pd.RangeIndex(2,10,2))









