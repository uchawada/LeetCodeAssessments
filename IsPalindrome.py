class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if str(x) == str(x)[::-1]:
            return True
        return False


Solution().isPalindrome('4567')