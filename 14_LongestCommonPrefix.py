from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ''
    first_word = strs[0]
    for i in range(len(first_word)):
        for s in strs:
            if i == len(s) or s[i] != first_word[i]:
                return prefix
        prefix += first_word[i]


strs = ["flower","flow","flight"]
longestCommonPrefix(strs)