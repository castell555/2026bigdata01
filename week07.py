import random

import numpy as np
import random as rnd

l1 = [9, '짬뽕', 3.7]
array02 = np.array(l1)
print(array02)

array03 = np.ones((2, 4), dtype=int)
print(array03)
print(array03.T)

l2 = list()
array04 = np.random.rand(2, 3)
print(array04)
print(array04.transpose())

l3 = []
for j in range(3):
    l2.append(random.random())
print(l2)
for item in l2:
    l3.append(item * 10)