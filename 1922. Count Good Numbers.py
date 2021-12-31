
# link - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def power(x, y, p) : # modular exponentiation
            res, x = 1, x % p
            
            if (x == 0) : return 0
        
            while (y > 0) :
                if ((y & 1) == 1) :
                    res = (res * x) % p
                y = y >> 1 
                x = (x * x) % p
                
            return res
            
        val = power(20, (n//2), (10**9 + 7)) * (5*(n%2) if n%2 else 1)

        return val % (10**9 + 7)
