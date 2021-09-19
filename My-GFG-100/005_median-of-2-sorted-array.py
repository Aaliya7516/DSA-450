def MedianOfArrays(array1, array2):
    array1 += array2
    array1.sort()
    l = len(array1)
    if l%2 == 0:
        return ('%g' % ((array1[l//2-1]+array1[l//2])/2))
    else:
        return (array1[l//2])

print(MedianOfArrays([1,5,9],[2,3,6,7]))
print(MedianOfArrays([4,6],[1,2,3,5]))
print(MedianOfArrays([4],[2]))