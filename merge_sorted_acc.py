def merge_two_arr(nums1, nums2):
    merged_arr = nums1 + nums2
    merged_arr = sorted(merged_arr)
    return merged_arr
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(merge_two_arr(nums1, nums2))
