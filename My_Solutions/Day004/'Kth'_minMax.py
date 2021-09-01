import heapq

arr = [2, 8, 7, 4, 5, 6, 23] #2,4,5,6,7,8, 23

def findKthLargest(nums, k):
    l = len(nums)
    print(l//2)
    if k < l//2:
        heapq.heapify(nums)
        print(" k < l//2")
        for i in range(l-k):
            heapq.heappop(nums)
    else :
        heapq._heapify_max(nums)
        print("else")
        for i in range(k+1):
            heapq.heappop(nums)
        
    return heapq.heappop(nums)

print(findKthLargest(arr, 3))