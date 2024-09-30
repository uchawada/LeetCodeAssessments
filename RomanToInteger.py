class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_map = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            value = symbol_map[s[i]]
            next_i = i+1
            if s[i] in symbol_map:
                if next_i < len(s) and symbol_map[s[i]] < symbol_map[s[next_i]]:
                    total -= value
                else:
                    total += value
        
        return total
                
        

#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

