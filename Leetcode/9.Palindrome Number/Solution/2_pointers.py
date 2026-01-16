class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        S = len(x)
        for i in range(S):
            j = S - 1 - i
            if x[i] != x[j]:
                return False
        return True
        