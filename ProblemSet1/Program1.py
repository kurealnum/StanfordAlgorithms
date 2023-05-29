def mergeSort(arr):
    if len(arr) <= 1:
         return arr, 0
    
    mid = len(arr)//2

    left, inv_count_left = mergeSort(arr[:mid])
    right, inv_count_right = mergeSort(arr[mid:])
    merged, inv_count_merge = merge(left, right, mid)

    total_inv_count = inv_count_left + inv_count_right + inv_count_merge
    return merged, total_inv_count


def merge(left_arr, right_arr, mid):
        #variables
        arr = [0]*(len(left_arr)+len(right_arr))
        i = j = k = 0
        split_inv = 0 

        #merge
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1

            else:
                arr[k] = right_arr[j]
                j += 1
                #the split inversions involving an element y of the 2nd array (right_arr) are 
                #exactly the numbers left in the 1st array B when y is copied to the output arr
                split_inv += mid - i

            k += 1

        #we could also just do arr += left_arr[i:] and vice versa
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr, split_inv

    
arr = []    


with open('IntegerArray.txt', mode="r") as f:
    for i in f:
        appendage = i[:len(i)-1]
        arr.append(appendage)



print(arr[len(arr)-2])

print(mergeSort(arr)[1])