#Function to return the count of number of elements in union of two arrays.
def doUnion(a,b):
    
    for i in a:
        if i not in b:
            b.append(i)
    
    a = []
    for i in b:
        if i not in a:
            a.append(i)
            
    return len(a)
        
print(doUnion([1, 2, 3, 4, 5], [1, 2, 3]))

# >>>>>>>>>>>>>>>> UNION with repeating characters <<<<<<<<<<<<<<<<<<<<<<<
# def doUnion(self,a,n,b,m):
    
#     #code here
#     a.sort()
#     b.sort()
#     hmap1 = {}
#     hmap2 = {}
    
#     for i in range(n):
#         if a[i] not in hmap1:
#             hmap1[a[i]] = 1
#         else:
#             hmap1[a[i]] += 1
#     for i in range(m):
#         if b[i] not in hmap2:
#             hmap2[b[i]] = 1
#         else:
#             hmap2[b[i]] += 1
            
#     ans = 0
#     if len(hmap1) < len(hmap2):
#         for i in hmap1:
#             if i in hmap2:
#                 if hmap1[i] > hmap2[i]:
#                     hmap2[i] = hmap1[i]
#             else:
#                 hmap2[i] = hmap1[i]
                
#         for i in hmap2:
#             ans += hmap2[i]
#     else:
#         for i in hmap2:
#             if i in hmap1:
#                 if hmap2[i] > hmap1[i]:
#                     hmap1[i] = hmap2[i]
#             else:
#                 hmap1[i] = hmap2[i]
                
#         for i in hmap1:
#             ans += hmap1[i]
            
#     return ans   
    