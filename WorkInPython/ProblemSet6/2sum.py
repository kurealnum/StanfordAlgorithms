#basically a binary search
def find_index_low(arr, start, end, t):
    # Where to insert a value
    if end == start:
        if arr[start] > t:
            return start
        else:
            return start+1
        
    mid = int((end+start)/2)
    center = arr[mid]
    
    if t > center:
        return find_index_low(arr, mid+1, end, t)
    else:
        return find_index_low(arr, start, mid, t)

#read the file
_arr = [int(i) for i in open("2sum.txt", "r").readlines()]
arr = sorted(_arr)

#init variables
c = 10000
n=len(arr)-1
mySum = {}

#main loop
for x in arr:
    mySet = set()

    i_low = find_index_low(arr, 0, n, -c - x)    
    i_up = find_index_low(arr, 0, n, c - x)
    
    mylist = arr[i_low:i_up]
        
    if x in mylist:
        mylist.remove(x)
    
    for m in mylist:
        mySum[x+m] = True
        
print (len(mySum.items()))

#credit to https://notebook.community/jazracherif/algorithms/2-sum/2-sum