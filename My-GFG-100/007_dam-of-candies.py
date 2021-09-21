def maxCandy(height):
    l = 0
    r = len(height)-1
    ans = 0
    while (l<r):
        area = min(height[l], height[r])*(r-l-1)
        ans = area if (area>ans) else ans
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return ans

print(maxCandy([1, 3, 4]))
print(maxCandy([2, 1, 3, 4, 6, 5]))
print(maxCandy([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(maxCandy([1, 3, 0, 5, 8, 5]))
print(maxCandy([2, 4, 6, 7, 9]))
print(maxCandy([100, 112, 256, 349, 770, 72, 86, 113, 119, 265, 445, 892]))
