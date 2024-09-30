class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        ds = []
        def findCombination(i, target):
            if i == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[i] <= target:
                ds.append(candidates[i])
                findCombination(i, target - candidates[i])
                ds.pop()
            findCombination(i + 1, target)
        findCombination(0, target)
        return ans



#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]
#Explanation:
#2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#7 is a candidate, and 7 = 7.
#These are the only two combinations.

