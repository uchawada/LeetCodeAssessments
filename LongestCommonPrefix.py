
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        shortest_word = min(strs)
        for i in range(len(shortest_word)):
            for word in strs:
                if word[i] != shortest_word[i]:
                    return res
            res += shortest_word[i]
        return res
        

strs = ["dog","racecar","car"]

Solution().longestCommonPrefix(strs)