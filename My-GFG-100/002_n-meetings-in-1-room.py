def maximumMeetings(n,start,end):
    count  = 1
    arr = [(i, j) for i,j in zip(start, end)]
    arr = sorted(arr, key = lambda x:x[1])
    s = 0
    for i in range(1, n):
        # print(i, " : ", arr, count, s)
        if arr[s][1] < arr[i][0]:
            count += 1
            s = i
    return count

print(maximumMeetings(6, [1,3,0,5,8,5],[2,4,6,7,9,9]))
print(maximumMeetings(3, [10, 12, 20],[20, 25, 30]))