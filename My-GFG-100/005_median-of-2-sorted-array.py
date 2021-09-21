def MedianOfArrays(array1, array2):
    i = 0
    j = 0
    m = len(array1)
    n = len(array2)
    temp = []
    while(i<m and j<n):
        if array1[i]<=array2[j]:
            temp.append(array1[i])
            i+=1
        else:
            temp.append(array2[j])
            j+=1

    if i == m:
        temp+= array2[j:]
    elif j == n:
        temp += array1[i:]

    if (m+n)%2 != 0:
        return temp[(m+n)//2]
    else:
        return ("%g" % ((temp[(m+n)//2-1]+temp[(m+n)//2])/2))


    # array1 += array2
    # array1.sort()
    # l = len(array1)
    # if l%2 == 0:
    #     return ('%g' % ((array1[l//2-1]+array1[l//2])/2))
    # else:
    #     return (array1[l//2])

print(MedianOfArrays([1,5,9],[2,3,6,7]))
print(MedianOfArrays([4,6],[1,2,3,5]))
print(MedianOfArrays([4],[2]))