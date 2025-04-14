from decimal import Decimal

cumsum = 0

def f(n): # factorial
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def ncr(n,r): # ncr
    return f(n) / (f(r) * f(n-r))

def s(n, k): # stirling number of the second kind, recursive implementation
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # S(0, 0) = 1

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    
    return dp[n][k]

for i in reversed(range(1, 1001)):
    p = Decimal(ncr(1000, i))*Decimal(f(i))*Decimal(s(1000, i))/Decimal(1000**1000)
    cumsum += p

    with open("186503.txt", "a") as g:
        g.write(f"{i} {cumsum}\n")
