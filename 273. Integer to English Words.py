# link - https://leetcode.com/problems/integer-to-english-words/

# space: O(1)
# time: O(log(n))

def base(num):
    name = {
        0:'',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety'
    }

    if num < 20:
        return name[num]
    elif num <= 99:
        temp = name[num//10 * 10]
        if num % 10:
            return temp + ' ' + base(num % 10)
        return temp
    else:
        temp = name[num//100] + ' Hundred'
        if num % 100:
            return temp + ' ' + base(num % 100)
        return temp

class Solution:
    def numberToWords(self, num: int) -> str:
        
        num = int(num)

        if num == 0: return 'Zero'

        thousands = {
            1: 'Thousand',
            2: 'Million',
            3: 'Billion',
            4: 'Trillion'
        }

        i, ans = 0, ''

        while (num):
            num, mod = divmod(num , 1000)
            value = base(mod).strip()
            if i and mod:
                value += ' ' + thousands[i]
            i += 1
            if value:
                ans = value + ' ' + ans
        
        return ans.strip()
