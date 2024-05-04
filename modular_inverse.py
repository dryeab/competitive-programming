N, MOD = 1005, 10 ** 9 + 7

factorial = [1] * (N + 1)
for i in range(1, N + 1):
    factorial[i] = (factorial[i-1] * i) % MOD 
    
inv_factorial = [1] * (N + 1)
inv_factorial[N] = pow(factorial[N], MOD-2, MOD)
for i in range(N-1, 0, -1):
    inv_factorial[i] = (inv_factorial[i+1] * (i+1)) % MOD 
    
def n_choose_k_mod(n, k):
    return (factorial[n] * inv_factorial[k] * inv_factorial[n-k]) % MOD 
