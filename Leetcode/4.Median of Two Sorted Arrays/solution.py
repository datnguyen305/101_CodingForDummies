class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = nums1 + nums2 
        total = sorted(total)
        n = len(total)
        def find_median(total):
            mid = n//2
            if len(total) % 2 != 0: 
                return total[mid]
            else: 
                cac = (total[mid] + total[mid-1])/2.0
                return cac

        return find_median(total)
