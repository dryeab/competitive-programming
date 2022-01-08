# link - https://leetcode.com/problems/capitalize-the-title/

# space: O(n)
# time: O(n*m) : m - average length of the strings

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        for i in range(len(title)):
            title[i] = title[i].title() if len(title[i]) > 2 else title[i].lower()
        return " ".join(title)
        
