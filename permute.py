"""
Basic list permutation
"""

import copy

def permute(arr, l, r):
    if l == r:
        yield copy.copy(arr)
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        yield from permute(arr, l + 1, r)
        arr[l], arr[i] = arr[i], arr[l]

string = 'ABC'
for p in permute(list(string), 0, len(string) - 1):
    print (p)
