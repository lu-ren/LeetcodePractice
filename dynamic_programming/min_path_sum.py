# https://leetcode.com/problems/minimum-path-sum/

def minimum_path_sum(m):
    dp = []
    for i in range(len(m)):
        dp.append([])
        for j in range(len(m[0])):
            dp[-1].append(float('inf'))

    for i in range(len(m)):
        for j in range(len(m[0])):
            v = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j] if i != 0 or j != 0 else m[i][j]
            dp[i][j] = v

    return dp[-1][-1]

m = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
]

print (minimum_path_sum(m))
