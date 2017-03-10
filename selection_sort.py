def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def selection_sort(A):
    for i in range(len(A)):
        least = i
        for j in range((i+1),len(A)):
            if A[j] < A[least]:
                least = j
        swap(A,least,i)

A = [3,6,1,8,4,5]       
selection_sort(A)
print(A)
