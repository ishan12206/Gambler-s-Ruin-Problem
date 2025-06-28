import numpy as np

def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    dp = [-1 for _ in range(N+1)] #initialise the distribution
    dp[0] = 1 #assume any value
    dp[1] = (1-r[0])/q[1] #compute in terms of preceding values
    
    for i in range(1,N):
        dp[i+1] = (dp[i]*(1-r[i]) - dp[i-1]*p[i-1])/q[i+1] #dynamic programming
    
    dp[N] = dp[N-1]*p[N-1] /(1 - r[N])#base case 

    s = sum(dp)
    for i in range(N+1):
        dp[i] = dp[i]/s #normalization

    return dp



def expected_time(p, q, r, N, a, b):
    """
    Return the expected time for the price to reach b starting from a.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """
    # Initialize base cases for the dp table
    dp = [[1, 0]] + [[None, None] for _ in range(1, N + 1)]
    dp[1] = [(1 - r[0]) / p[0], -1 / p[0]]

    # Populate dp table using the recurrence relation
    for k in range(2, b + 1):
        factor = (1 - r[k - 1]) / p[k - 1]
        dp[k][0] = factor * dp[k - 1][0] - (q[k - 1] / p[k - 1]) * dp[k - 2][0]
        dp[k][1] = factor * dp[k - 1][1] - (q[k - 1] / p[k - 1]) * dp[k - 2][1] - 1 / p[k - 1]

    # Compute `a_val` after filling the dp table
    a_val = -dp[b][1] / dp[b][0]

    # Generate the list `E` with computed values
    E = [a_val * dp[k][0] + dp[k][1] for k in range(b + 1)]

    # Return the element at index `a` in `E`
    return E[a]
            


