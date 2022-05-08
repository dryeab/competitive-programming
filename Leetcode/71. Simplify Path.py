# link - https://leetcode.com/problems/simplify-path/

# space: O(n)
# time: O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        i = j = 0
        while j <= len(path):
            if j == len(path) or path[j] == '/':
                directory = path[i+1:j]
                if directory:
                    if directory == '..':
                        if answer:
                            answer.pop()
                    elif directory != '.':
                        answer.append(directory)
                i = j
            j += 1
        return "/" + "/".join(answer)
