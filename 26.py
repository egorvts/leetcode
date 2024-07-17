class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        res = 1
        for i in range(1, len(nums)):
            print(nums)
            if (nums[i] <= nums[i-1]) and (i != len(nums) - 1):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                res += 1

        return res
