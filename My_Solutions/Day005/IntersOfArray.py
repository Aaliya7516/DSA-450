def intersection( nums1, nums2):
        
    nums1 = set(nums1)
    
    ans = []
    for i in nums2:
        if i in nums1:
            ans.append(i)
            nums1.remove(i)
    
    return ans

print(intersection([1, 2, 3, 4, 5], [1, 2, 2, 9]))

    # i = 0
    # while (i < len(nums1)):
    #     if nums1[i] not in nums2:
    #         nums1.remove(nums1[i])
    #         i -= 1
    #     i += 1
    # i = 0
    # while (i < len(nums2)):
    #     if nums2[i] not in nums1:
    #         nums2.remove(nums2[i])
    #         i -= 1
    #     i += 1
    # nums1 = []    
    # for i in nums2:
    #     if i not in nums1:
    #         nums1.append(i)        
    # return nums