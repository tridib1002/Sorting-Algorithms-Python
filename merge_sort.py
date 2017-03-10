def mergeSort(A):
	if len(A)>1:
		mid = len(A)//2
		
		lefthalf = A[:mid]
		rightHalf = A[mid:]

		mergeSort(lefthalf)
		mergeSort(rightHalf)

		i = 0
		j = 0
		k = 0
		
		while i<len(lefthalf) and j<len(rightHalf) :
			if lefthalf[i] < rightHalf[j]:
				A[k] = lefthalf[i]
				i = i+1
			else:
				A[k] = rightHalf[j]
				j = j+1
			k = k+1

		while(i<len(lefthalf)):
			A[k] = lefthalf[i]
			i = i+1
			k = k+1

		while (j<len(rightHalf)):
			A[k] = rightHalf[j]
			j = j+1
			k = k+1

A = [54,26,93,17,77,31,44,55,20]
mergeSort(A)
print(A)
