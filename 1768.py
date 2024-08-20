class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
        if i >= len(word1):
            res += word2[j:]
        else:
            res += word1[i:]
        return res
