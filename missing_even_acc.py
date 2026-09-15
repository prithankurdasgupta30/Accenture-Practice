def missingEven(nums):
        res = []
        for i in range(1, len(nums)):
                diff = nums[i] - nums[i-1]
                if diff > 2:
                        for j in range(nums[i-1]+2, nums[i], 2):
                                res.append(j)
        return res
nums = list(map(int, input().split(",")))
print(missingEven(nums))