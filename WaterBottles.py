class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drank_bottles = 0
        total_empty_bottles = 0
        
        while numBottles > 0:
            total_drank_bottles +=1
            total_empty_bottles += 1
            
            # if a total of numExchange empty bottles, add 1 to the numBottles
            if total_empty_bottles % numExchange == 0:
                numBottles += 1
                
            numBottles -=1

        return total_drank_bottles

#Input: numBottles = 9, numExchange = 3
#Output: 13
#Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
#Number of water bottles you can drink: 9 + 3 + 1 = 13.

