"""
Leetcode: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
"""

from collections import Counter

def min_domino_rotations(A, B):
    length = len(A)
    dom_cnt = Counter()

    for a, b in zip(A, B):
        if a == b:
            dom_cnt[a] += 1
        else:
            dom_cnt[a] += 1
            dom_cnt[b] += 1

    sixes = set([k for (k, v) in dom_cnt.items() if v == length])

    if not sixes:
        return -1

    A_freq = Counter(A)
    B_freq = Counter(B)

    min_rot = float('inf')

    for six in sixes:
        min_rot = min(length - A_freq[six], length - B_freq[six])
    return min_rot

A, B = [2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]
print (min_domino_rotations(A, B))
A, B = [3, 5, 1, 2, 3], [3, 6, 3, 3, 4]
print (min_domino_rotations(A, B))

A, B = [1, 1, 1, 1], [1, 1, 1, 1]
print (min_domino_rotations(A, B))
