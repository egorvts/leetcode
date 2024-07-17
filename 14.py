class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for _ in range(len(min(strs, key=len))):
            if len(set(map(lambda x: x[len(res)], strs))) == 1:
                res += strs[0][len(res)]
        
        return res
    