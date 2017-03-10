def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def bubble_sort(A):
    for i in range(len(A)):
        flag = 0
        for j in range (len(A)-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                flag = 1
        if flag == 0:
            break

A = [3,6,1,8,4,5]
bubble_sort(A)
print(A)