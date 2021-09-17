def sort012(arr):
    l = 0
    m = 0
    h = len(arr)-1
    while (m <= h):
        if arr[m] == 0:
            arr[m], arr[l] = arr[l], arr[m]
            l += 1
            m += 1
            
        elif arr[m] == 1:
            m += 1
            
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    
    return arr

print(sort012([0,2,1,2,0,1,1,2,0,0]))
print(sort012([0, 2, 1, 2, 0]))
print(sort012([0, 1, 0]))
