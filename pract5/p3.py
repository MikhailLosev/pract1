def candies(n:int, k:int)->int:
        if k > n:
            return "No solution"

        dp = [[1] * n for a in range(n)]

        for c in range(2, n):
            for b in range(1,min(c,k)):
                dp[c][b] = dp[c-1][b-1] + dp[c-1][b] * (b+1)
        return dp[n-1][k-1]

def main():
    print(candies(4,7))
    print(candies(15,9))

if __name__ == "__main__":
    main()
