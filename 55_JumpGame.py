class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = nums[len(nums)-1]

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0



# nums = [2, 3, 1, 1, 4]
nums = [3,2,1,0,4]
print(Solution().canJump(nums))
            
        