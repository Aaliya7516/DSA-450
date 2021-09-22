def sol (A):
	n = len(A)
	ans  = [0]*n
	ans[0] = 1
	for i in range(1,n):
		ans[i] = ans[i-1]*A[i-1]
	
	r = 1
	for i in range(n-1, -1, -1):
		ans[i] *= r
		r *= A[i]

	return ans
print(sol([1,1,2,1,1,0,1]))
print(sol([1,0,1,1,0,1]))

