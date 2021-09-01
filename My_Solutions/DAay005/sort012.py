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

print(sort012([0,2,1,2,0,1,1,2,0,0,]))
    # code here
    
    # zero = 0
    # one = 0
    # two = 0
    
    # for i in arr:
    #     if i == 0:
    #         zero+= 1
    #     if i == 1:
    #         one+= 1
    #     if i == 2:
    #         two+= 1
            
    # arr = [0]*zero + [1]*one + [2]*two
    # return arr