from collections import Counter
def identicalBlock(nums):
        freq = Counter(nums)
        res = []
        for num, count in freq.items():
                if num != count:
                        res.append(num)
        return res
nums = list(map(int, input().split(",")))
print(identicalBlock(nums)) 