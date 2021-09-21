# TC = O(log n); SC = O(1)

def binarySearch(A, e):
    l = 0
    r = len(A)-1
    while(l<=r):
        if A[l] == e:
            return l
        if A[r] == e:
            return r
        m = l + (r-l)//2
        if A[m] == e:
            return m
        if A[m] > e:
            r = m-1
        else:
            l = m+1
    return -1

print(binarySearch([1, 2, 3, 4, 6, 7, 8, 9, 10], 2))
print(binarySearch([1, 2, 3, 4, 6, 7, 8, 9, 10], 10))
print(binarySearch([1, 2, 3, 4, 6, 7, 8, 9, 10], 4))
print(binarySearch([1, 2, 3, 4, 6, 7, 8, 9, 10], 5))