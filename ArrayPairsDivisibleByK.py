
from collections import defaultdict

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        
        remainder_freq = defaultdict(int)
        for num in arr:
            rem = (num%k + k) % k
            remainder_freq[rem] += 1


        if remainder_freq.get(0) is not None:
            if remainder_freq[0]%2 != 0:
                return False
        
        for remainder in range(1, (k//2)+1):
            counter = k - remainder
            if remainder_freq[counter] != remainder_freq[remainder]:
                return False
        return True


arr = [1,2,3,4,5,10,6,7,8,9]
# arr = [-1,-1,-1,-1,2,2,-2,-2]
# k = 3
k = 5

print(Solution().canArrange(arr, k))

