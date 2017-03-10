def insertion_sort(A):
	for i in range(1,len(A)):
		temp = A[i]
		hole = i
		while hole > 0 and temp < A[hole-1]:
			A[hole] = A[hole-1]
			hole -= 1
		A[hole] = temp

A = [3,6,1,8,4,5]
insertion_sort(A)
print(A)
