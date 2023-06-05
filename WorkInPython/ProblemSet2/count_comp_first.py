#there are 3 programs in this problem set, all of them revolve around the pivot choice

def quick_sort(A,l,r, count):
    if l <= r:

        i = choose_pivot(A,l,r)

        temp = A[l]
        A[l] = A[i]
        A[i] = temp

        j = partition(A,l,r)
        
        l_array_len = quick_sort(A,l,j-1, count)
        r_array_len = quick_sort(A,j+1,r, count)

        count += (r-l) + l_array_len + r_array_len

        return count

    #redundant, but easier to read and understand
    else:
        return 0
 
 
def partition(A,l,r):
    #base variables
    p = A[l]
    i = l+1
    j = l+1
 
    #main partition
    while j <= r:
        if A[j] < p:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
 
            i += 1

        j += 1
 
    temp = A[l]
    A[l] = A[i-1]
    A[i-1] = temp
 
    return i-1
 
 
def choose_pivot(A,l,r):
    return l
 
 
fp = open("C:\Code\Python\StanfordAlgorithms\ProblemSet2\quickSort.txt", 'r')
data = fp.readlines()
A = [int(x.strip()) for x in data]

#comparison counter
count = 0
l = 0
r = len(A)-1
 
print(quick_sort(A,l,r, count))
