class Solution(object):
    def findClosestNumber(self, nums):
        gap, num = abs(nums[0]), nums[0]
        for n in nums:
            if abs(n) < gap:
                gap = abs(n)
                num = n
            elif abs(n) == gap and n > num:
                num = n
        return num
