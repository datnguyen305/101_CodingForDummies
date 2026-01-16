class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        S = len(s)
        total = 0
        prev = 0 
        for i in range(S - 1, -1, -1):
            curr = number_dict[s[i]]
            if curr >= prev: 
                total += curr
            elif curr < prev:
                total -= curr
            prev = curr
        return total

# Out of bounce :3
"""
class Solution(object):
    def romanToInt(self, s):
        :type s: str
        :rtype: int
        number_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        S = len(s)
        total = 0
        for i in range(S - 1, -1, -1):
            if number_dict[s[i]] >= number_dict[s[i-1]]: 
                total += number_dict[s[i]]
            elif number_dict[s[i]] < number_dict[s[i-1]]:
                total -= number_dict[s[i]]
        return total
"""

