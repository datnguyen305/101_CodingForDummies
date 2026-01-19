class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        
        def LCP(left, right):
            l_min = min(len(left), len(right))
            for i in range(l_min):
                if left[i] != right[i]:
                    return left[:i]
            return left[:l_min]

        def divide_and_conquer(strs, l, r):
            if l == r: 
                return strs[l]
            mid = (l+r)//2
            left = divide_and_conquer(strs, l, mid)
            right = divide_and_conquer(strs, mid+1, r)
            return LCP(left, right)
        return divide_and_conquer(strs, 0, len(strs) - 1)