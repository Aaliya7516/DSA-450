def partition(arr,l,r):
    x = arr[r]
    i = l
    for j in range(l,r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
    
def findKthLargest(arr, l, r, k):
    if l == r:
        return arr[l]
    index = partition(arr,l,r)
    if index == k:
        return arr[k]
    elif index > k:
        return findKthLargest(arr, l, index-1, k)
    else:
        return findKthLargest(arr, index+1, r, k-index-1)

def kthElement( arr1, arr2, k):
    arr1 += arr2
    return findKthLargest(arr1, 0, len(arr1)-1, k-1)
        
print(kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))
print(kthElement([100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892], 7))
