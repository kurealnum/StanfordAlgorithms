#there are 3 programs in this problem set, all of them revolve around the pivot choice

def quick_sort(A,l,r, count):
    if l <= r:

        i = choose_pivot(A,l,r)

        temp = A[l]
        A[l] = A[i]
        A[i] = temp

        j = partition(A,l,r)

        #minus 1 cause we're just adding them to the comparison count
        
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
    n = r - l + 1 # num of points
    if n%2 == 0:
        m= l + int(n/2) - 1
    else:
        m= l + int(n/2)
    
    if (A[m] > A[l] and A[m] < A[r]) or (A[m] > A[r] and A[m] < A[l]): 
        return m
    elif (A[l] > A[m] and A[l] < A[r]) or (A[l] > A[r] and A[l] < A[m]): 
        return l
    else:
        return r
 
 
fp = open("C:\Code\Python\StanfordAlgorithms\ProblemSet2\quickSort.txt", 'r')
data = fp.readlines()
A = [int(x.strip()) for x in data]

#comparison counter
count = 0
l = 0
r = len(A)-1
 
print(quick_sort(A,l,r, count))
