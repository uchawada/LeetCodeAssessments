class MedianFinder(object):

    def __init__(self):
        # Max heap for the lower half
        self.lower_half = []  # Max heap (invert values to use min heap)
        # Min heap for the upper half
        self.upper_half = []  # Min heap

    def addNum(self, num):
        # Add to max heap (lower half)
        heapq.heappush(self.lower_half, -num)
        
        # Ensure max of lower half is less than or equal to min of upper half
        if (self.lower_half and self.upper_half and 
            (-self.lower_half[0] > self.upper_half[0])):
            # Move the largest of the lower half to the upper half
            value = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, value)

        # Balance the sizes of the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            # Move the largest from lower half to upper half
            value = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, value)
        elif len(self.upper_half) > len(self.lower_half):
            # Move the smallest from upper half to lower half
            value = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -value)

    def findMedian(self):
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])  # max of lower half
        return (-self.lower_half[0] + self.upper_half[0]) / 2.0  # mean of max of lower half and min of upper half

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
#[[], [1], [2], [], [3], []]

