def mergeSort(arr):
    if len(arr) <= 1:
         return arr, 0
    
    mid = len(arr)//2

    left, inv_count_left = mergeSort(arr[:mid])
    right, inv_count_right = mergeSort(arr[mid:])
    merged, inv_count_merge = merge(left, right)

    total_inv_count = inv_count_left + inv_count_right + inv_count_merge
    return merged, total_inv_count


def merge(left_arr, right_arr):
        #merge
        arr = [0]*(len(left_arr)+len(right_arr))
        i = j = k = 0
        split_inv = 0 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1

            else:
                arr[k] = right_arr[j]
                j += 1
                split_inv += len(left_arr) - i 

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
    
    
arr = [6,5,4,3,2,1]

print(mergeSort(arr))