# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        low = 2
        high = n
        while low <= high:
            middle = (low + high) // 2
            if isBadVersion(middle) and not isBadVersion(middle - 1):
                return middle
            elif not isBadVersion(middle) and not isBadVersion(middle - 1):
                low = middle + 1
            else:  # isBadVersion(middle) and isBadVersion(middle - 1)
                high = middle - 1
