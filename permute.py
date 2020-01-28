"""
Basic list permutation
"""

import copy

def permute(arr, l):
    if l == len(arr) - 1:
        yield copy.copy(arr)
    for i in range(l, len(arr)):
        arr[l], arr[i] = arr[i], arr[l]
        yield from permute(arr, l + 1)
        arr[l], arr[i] = arr[l], arr[i]

string = 'ABC'
for p in permute(list(string), 0):
    print (p)
