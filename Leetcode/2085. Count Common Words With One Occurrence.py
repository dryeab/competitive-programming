
# link - https://leetcode.com/problems/count-common-words-with-one-occurrence/

# space: O(n + m)
# time: O(n + m)

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer, count1, count2 = 0, Counter(words1), Counter(words2)
        for word in count1:
            if count1[word] == count2[word] == 1:
                answer += 1
        return answer
