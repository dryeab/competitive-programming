
# link - https://leetcode.com/problems/pancake-sorting

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        i = 0

        ans = []

        while(i < len(arr)):
            
            max_index = 0
            for j in range(len(arr) - i):
                if arr[max_index] < arr[j]:
                    max_index = j
            
            if max_index == 0:
                arr[:n-i] = arr[:n-i][::-1]
                ans.append(n-i)
            elif max_index == n - i:
                i += 1
                continue;
            else:
                arr[:max_index+1] = arr[:max_index+1][::-1]
                ans.append(max_index+1)
                arr[:n-i] = arr[:n-i][::-1]
                ans.append(n-i)
                
            i += 1
            
        return ans
        
