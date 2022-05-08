
# link - https://leetcode.com/problems/fruit-into-baskets/

# space: O(1)
# time: O(n)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, basket = 0, {}
        i = j = 0
        while j < len(fruits):
            if fruits[j] in basket:
                basket[fruits[j]] += 1
            else:
                if len(basket) == 2:
                    ans = max(ans, j-i)
                    while basket[fruits[i]] != 1:
                        basket[fruits[i]] -= 1
                        i += 1
                    basket.pop(fruits[i])
                    i += 1
                basket[fruits[j]] = 1
            j += 1
        ans = max(ans, j-i)
        return ans
