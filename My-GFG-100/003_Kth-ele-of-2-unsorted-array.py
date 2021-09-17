import heapq
def findKthLargest(nums, k):
    l = len(nums)
    heapq.heapify(nums)
    for i in range(k):
        heapq.heappop(nums)
    
    return heapq.heappop(nums)

def kthElement( arr1, arr2, k):
    arr1 += arr2
    return findKthLargest(arr1, k-1)
        
print(kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))
print(kthElement([100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892], 7))
