def divide_n_conquer(nums, left, right):
    # base case
    if left == right:
        return nums[left]
    p = (left + right) // 2

    left_sum = divide_n_conquer(nums, left, p)
    right_sum = divide_n_conquer(nums, p + 1, right)
    cross_sum = cross_sum_fn(nums, left, right, p)

    return max(left_sum, right_sum, cross_sum)

# start at p, go left to beginning finding max_left_sum
# then go right from p to the end finding max_right_sum
# then return max_left_sum + max_right_sum
def cross_sum_fn(nums, left, right, p):

    max_left_sum = float('-inf')
    max_right_sum = float('-inf')
    cur = 0

    for i in range(p, left - 1, -1):
        cur += nums[i]
        max_left_sum = max(cur, max_left_sum)

    cur = 0
    for i in range(p + 1, right + 1):
        cur += nums[i]
        max_right_sum = max(cur, max_right_sum)
    return max_left_sum + max_right_sum

# Kadane's algorithm based on the following formula:
# dp[i] = max(dp[i-1], 0) + arr[i]
def kadane(arr):
    dp = [arr[0]]

    for i in range(1, len(arr)):
        dp.append(max(dp[i - 1], 0) + arr[i])
    print(dp)
    return max(dp)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print (divide_n_conquer(arr, 0, len(arr) - 1))
print (kadane(arr))
arr = [0, 1, 2, 3, -1]
print (kadane(arr))
arr = [-1, 0, 1, 2, 3]
print (kadane(arr))
