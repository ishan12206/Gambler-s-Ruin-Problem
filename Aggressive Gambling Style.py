"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral) :       
        rem = Integral % 2
        binary += str(rem);  
        Integral //= 2

    binary = binary[ : : -1]  
    binary += '.'

    while (k_prec) : 
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) :  
            fractional -= fract_bit  
            binary += '1'       
        else : 
            binary += '0'
        k_prec -= 1
        
    return binary 

def win_probability(p, q, k, N):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """

    dp = [0 for _ in range(N+1)]
    dp[0] = 0
    dp[N] = 1
    for i in range(N-1,1,-1):
        if i < N//2:
            dp[i] = dp[2*i]*p
        elif i >= N//2:
            dp[i] = p + q*dp[2*i-N]
    
    return dp[k]


def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    
    dp = [0 for _ in range(N+1)]
    for i in range(N-1,1,-1):
        if i < N//2:
            dp[i] = 1 + dp[2*i]*p
        elif i >= N//2:
            dp[i] = 1 + q*dp[2*i-N]
    
    return dp[k]
    

        

