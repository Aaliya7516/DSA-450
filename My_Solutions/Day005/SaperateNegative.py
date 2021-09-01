def rearrange(arr, n):

    l = 0
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1

    return arr

    # l = 0
    # m = 0
    # h = n-1

    # while m <= h:
    #     if arr[m] < 0:
    #         arr[m], arr[l] = arr[l], arr[m]
    #         l += 1
    #         m += 1
    #     else:
    #         arr[m], arr[h] = arr[h], arr[m]
    #         h -= 1
    #     print(arr)

    # return arr

arr = [2, -3, 4, 5, 9, -2]
n = len(arr)
print(rearrange(arr, n))
 