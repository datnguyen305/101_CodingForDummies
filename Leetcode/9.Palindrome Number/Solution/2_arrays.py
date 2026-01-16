class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        S = len(x)
        pivot = S // 2  
        array_1 = []
        array_2 = []    
        for i in range(0, pivot):
            array_1.append(x[i])
        for i in range(S-pivot, S):
            array_2.append(x[i])
        array_2 = array_2[::-1]
        for i, j in zip(array_1, array_2):
            if i != j:
                return False
        return True
         