
# link - https://leetcode.com/problems/replace-words/

# space: O(n+m)
# time: O(n+m)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        answer, dictionary = sentence.split(), set(dictionary)
        for j in range(len(answer)):
            word = answer[j]
            for i in range(len(word)):
                if word[:i+1] in dictionary:
                    answer[j] = word[:i+1]
                    break;
        return " ".join(answer)
