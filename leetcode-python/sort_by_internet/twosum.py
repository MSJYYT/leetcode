'''example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''

class Solution():
    def twoSum(nums,target):
        d = {}
        size = 0
        while size < len(nums):
            if not nums[size] in d:
                d[nums[size]] = size
            if target - nums[size] in d:
                if d[target-nums[size]] < size :
                    ans = [d[target - nums[size]], size ]
                    return ans
            size = size+1

print(Solution.twoSum([2, 7, 11, 15],9))