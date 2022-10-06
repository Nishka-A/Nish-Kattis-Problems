import sys
 
def f(idx, prev_idx, n, a,dp):
 
    if (idx == n):
        return 0
 
    if (dp[idx][prev_idx + 1] != -1):
        return dp[idx][prev_idx + 1]
 
    notTake = 0 + f(idx + 1, prev_idx, n, a, dp)
    take = -sys.maxsize -1
    if (prev_idx == -1 or a[idx] > a[prev_idx]):
        take = 1 + f(idx + 1, idx, n, a, dp)
 
    dp[idx][prev_idx + 1] = max(take, notTake)
    return dp[idx][prev_idx + 1]
 
# Function to find length of longest increasing
# subsequence.
def longestSubsequence(n, a):
 
    dp = [[-1 for i in range(n + 1)]for j in range(n + 1)]
    return f(0, -1, n, a, dp)
 
# Driver program to test above function
s = raw_input()
a = []
for i in s:
    a.append(int(ord(i) - 96))

n = len(a)
print(26 - longestSubsequence(n, a))
