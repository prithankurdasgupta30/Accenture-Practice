def largeSmallSum(arr):
        length = len(arr)
        even_arr = []
        odd_arr = []
        for i in range(length):
                if i % 2 == 0:
                        even_arr.append(arr[i])
                else:
                        odd_arr.append(arr[i])
        even_arr = sorted(even_arr)
        odd_arr = sorted(odd_arr)
        return (even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])
arr = list(map(int, input().split()))
print(largeSmallSum(arr))