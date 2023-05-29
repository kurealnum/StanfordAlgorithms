def quick_sort(A,l,r):
    if len(A) < 1:
        i = choose_pivot(A,l,r)

        temp = A[l]
        A[l] = A[i]
        A[i] = temp

        j = partition(A,l,r)
        
        quick_sort(A,l,j-1)
        quick_sort(A,j+1,r)


def partition(A,l,r):
    pass


def choose_pivot(A,l,r):
    pass