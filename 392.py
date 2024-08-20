class Solution(object):
    def isSubsequence(self, s, t):
        sIndex = 0
        for i in t:
            if i == s[sIndex]:
                sIndex += 1
                if sIndex == len(s):
                    return True
        return False
    
solution = Solution
print(solution.isSubsequence(solution, "", "ahbgdc"))