def querySum(arr, q, queries):
    
    ans = []
    for i in range(q):
        l = queries[i*2]
        r = queries[i*2+1]
        sums = 0
        for j in range(l-1,r):
            sums += arr[j]
        ans.append(sums)
    return ans

print(querySum([1, 2, 3, 4],2,[1, 4, 2, 3]))