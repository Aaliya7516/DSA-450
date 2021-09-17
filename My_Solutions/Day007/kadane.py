def maxSubArray(nums):
    sums = 0
    maxi = -9999999
    
    for i in range(len(nums)):
        sums+=nums[i]
        if(sums>maxi):
            maxi = sums
        if(sums<0):
            sums = 0  
            
    return maxi

print(maxSubArray([2, -3, 4, 5, 9, -2]))