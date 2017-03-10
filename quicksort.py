def swap(A,x,y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp

def quickSort(A,lo,hi):
	if lo < hi:
		pIndex = partition(A,lo,hi)
		quickSort(A,lo,pIndex-1)
		quickSort(A,pIndex+1,hi)

def partition(A,lo,hi):
	pIndex = lo
	pivot = A[hi]
	for i in range(lo,hi):
		if A[i] <= pivot:
			swap(A,pIndex,i)
			pIndex += 1
	swap(A,pIndex,hi)
	return pIndex

A = [5,7,9,8,2,4,3,1,6]

quickSort(A,0,len(A)-1)

print(A)