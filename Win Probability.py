def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    return (1 - (q/p)**k) / (1 - (q/p)**N) if p!=q else k/N

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p > q:
        return (1 - (q/p)**k)
    elif p <= q:
        return 0

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p==q:
        return k*(N-k)
    else:
        return k/(q-p) - (N)/(q-p) * ((1 - (q/p)**k) / (1 - (q/p)**N))
    
    
