class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList) 
        if endWord not in wordSet:
            return 0

        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        queue = deque([(beginWord, 1)])

        while queue:
            current_word, count = queue.popleft()

            for i in range(len(current_word)):
                for c in alphabets:
                    new_word = current_word[:i] + c + current_word[i + 1:]

                    if new_word == endWord:
                        return count + 1 

                    if new_word in wordSet:
                        queue.append((new_word, count + 1))
                        wordSet.remove(new_word)

        return 0


#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5
#Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

