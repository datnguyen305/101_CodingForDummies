class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: 
            return ""
        start, end = 0, 0 
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            odd_len = expand(i,i)
            even_len = expand(i, i + 1)
            max_length = max(odd_len, even_len)
            
            if max_length > (end - start):
                start = i - (max_length - 1) // 2
                end = i + max_length // 2 
        return s[start:end + 1]