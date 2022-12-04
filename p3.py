def candies(n, k):
    if k > n:
        return "No solution"

    dp = [[1] * n for a in range(n)]

    for c in range(2, n):
        for b in range(1,min(c,k)):
            dp[c][b] = dp[c-1][b-1] + dp[c-1][b] * (b+1)
    return dp[n-1][k-1]
print(candies(4,7 ))
