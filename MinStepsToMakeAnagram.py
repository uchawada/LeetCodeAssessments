from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        min_steps = 0
        
        for letter in s_counter.keys():
            s_count = s_counter[letter]
            t_count = t_counter[letter]
            
            if s_count == t_count:
                continue
            if s_count > t_count:
                min_steps += s_count - t_count
        

        return min_steps




#Input: s = "leetcode", t = "practice"
#Output: 5
#Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
#Example 3:


