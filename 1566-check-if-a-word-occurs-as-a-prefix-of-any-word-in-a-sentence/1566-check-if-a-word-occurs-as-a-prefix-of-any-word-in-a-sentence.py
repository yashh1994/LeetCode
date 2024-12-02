class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        ans = 0
        for i in range(len(words)):
            w = words[i]
            if w[:len(searchWord)] == searchWord:
                return i+1
        return -1
        