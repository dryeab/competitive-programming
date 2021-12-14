# link - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums):
        snums = [str(num) for num in nums]

        result = [None] * len(nums)

        for i in range(len(nums)):
            
            m = 0
            for j in range(len(nums)):
                one = snums[m] + snums[j]
                two = snums[j] + snums[m]
                
                if int(snums[m] + snums[j]) < int(snums[j] + snums[m]):
                    m = j

            result[i] = snums[m]
            snums[m] = "0"
        
        return str(int("".join(result)))
            


