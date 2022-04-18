# Given an array arr of size N and an integer K. The task is to find the pair of integers in the array such that their sum is maximum but less than K.

# Note:Out of every possible pair, find pair with a maximum absolute difference.

# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow.
# The first line of each test case contains N and K, where N is the number of elements in the array and K is the bound. The second line of each test case contains the array elements.

# Output:
# Print the pair with the maximum sum less than K.

# Your task:
# You don't have to take input. Complete the function Max_Sum(), which takes the array, N and K as parameters and returns the pair of integer if exist else return pair of zeros (0,0). The printing is done by the driver code. 

# Constraints:
# 1 ≤ T ≤ 10
# 0 ≤ N ≤ 105
# 0 ≤ K ≤ 106
# 0 ≤ arr[i] ≤ 105

# Example:
# Input:
# 2
# 6 10
# 2 3 4 6 8 10
# 6 0
# 2 3 4 6 8 10
# Output:
# 3 6
# 0 0

# Explanation:
# Testcase 1: Pair (3,6) has a maximum sum equals 9 which is less than 10.
# Testcase 2: There doesn't exist any pair in the array with a sum less than 0.

# ---------------------------------- SOLUTION -------------------------------------------- >> GFG

def Max_Sum(arr,n,k):
    arr.sort()
    l = 0
    r = n-1
    ans = [0,0]
    while(l<r):
        if arr[l]+arr[r] < k:
            if ans[0]+ans[1] < arr[l]+arr[r]:
                ans[0] = arr[l]
                ans[1] = arr[r]
            l += 1
        else:
            r -= 1
    return ans
