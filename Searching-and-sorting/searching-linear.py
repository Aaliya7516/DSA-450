# TC = O(n); SC = O(1)

def linearSearch(A, e):
    l = 0
    r = len(A)-1
    while(l<=r):
        if A[l] == e:
            return l
        if A[r] == e:
            return r
        l += 1
        r -= 1
    return -1

print(linearSearch([2, 3, 6, 7, 9, 1, 4, 8, 10], 2))
print(linearSearch([2, 3, 6, 7, 9, 1, 4, 8, 10], 10))
print(linearSearch([2, 3, 6, 7, 9, 1, 4, 8, 10], 4))
print(linearSearch([2, 3, 6, 7, 9, 1, 4, 8, 10], 5))