def quick_sort(A,l,r):
    if l < r:
        print(A)

        j = partition(A,l,r)
        
        quick_sort(A,l,j-1)
        quick_sort(A,j+1,r)


def partition(A,l,r):
    #base variables
    p = A[l]
    i = l+1

    #main partition
    for h in range(l,r):
        if A[h] <= p:
            temp = A[i]
            A[i] = A[h]
            A[h] = temp

            i += 1

    temp = A[l]
    A[l] = A[i-1]
    A[i-1] = temp

    return i-1


def choose_pivot(A,l,r):
    #there are 3 programs in this problem set, all of them revolve around the pivot choice
    return 0


A = [3,4,2,1]
l = 0
r = len(A)-1

quick_sort(A,l,r)
print(A)