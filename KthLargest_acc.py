import heapq
def KthLargest(arr,k):
        minHeap = []
        for num in arr:
                heapq.heappush(minHeap, num)
                if len(minHeap) > k:
                        heapq.heappop(minHeap)
        return minHeap[0]
arr = list(map(int, input().split()))
k = int(input())
print(KthLargest(arr,k))