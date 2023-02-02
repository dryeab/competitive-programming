class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter, digit = [], []
        for log in logs:
            is_digit = False
            for i in range(log.index(' '), len(log)):
                is_digit = is_digit or log[i].isdigit()
            (digit if is_digit else letter).append(log)
        
        letter.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        
        return letter + digit