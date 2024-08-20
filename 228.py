class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - end == 1:
                end = nums[i]
            else: 
                if start != end:
                    print(start, end)
                    res.append(f"{start}->{end}")
                else:
                    res.append(f"{start}")
                start = end = nums[i]

        if start != end:
            print(start, end)
            res.append(f"{start}->{end}")
        else:
            res.append(f"{start}")
        return res
    