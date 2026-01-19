"""
   Lấy chữ đầu làm mốc rồi so sánh với các chữ còn lại
   Nếu khác thì trả về chuỗi từ đầu đến vị trí khác
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            prefix = strs[0][i]
            for word in strs[1:]:
                if len(word) == 0:
                    return ""
                elif i >= len(word) or word[i] != prefix:
                    return strs[0][:i]
        return strs[0] 