import java.util.Arrays;

public class countInversions {

    //main process
    public static void main(String[] args) {
        Integer[] arr = new Integer[]{3,4,2,1};

        returnTwo res_arr = mergeSort(arr, 0);
        int inver_count = mergeAndCountInversions(arr);

        System.out.println(Arrays.toString(res_arr.returnArr)); 
        System.out.println(inver_count);
    }


    public static int mergeAndCountInversions(Integer[] arr) {
        if (arr.length > 1) {
            Integer l = 0;
            Integer r = arr.length-1;

            Integer[] leftArr = Arrays.copyOfRange(arr, l, Math.floorDiv(r, 2)+1);
            Integer[] rightArr = Arrays.copyOfRange(arr, Math.floorDiv(r, 2)+1, r+1);

            int left_inversions = mergeAndCountInversions(leftArr);
            int right_inversions = mergeAndCountInversions(rightArr);
            returnTwo split_inversions = mergeSort(arr, 0);

            int total_inversions = left_inversions + right_inversions + split_inversions.inver_count;

            return total_inversions;
        }

        return 0;
    }


    public static returnTwo mergeSort(Integer[] arr, int inver_count) {
        if (arr.length > 1) {
            //variables for simplicity 
            Integer l = 0;
            Integer r = arr.length-1;

            Integer[] returnArr = new Integer[arr.length];
            Integer[] leftArr = Arrays.copyOfRange(arr, l, Math.floorDiv(r, 2)+1);
            Integer[] rightArr = Arrays.copyOfRange(arr, Math.floorDiv(r, 2)+1, r+1);

            //recursive function calls
            leftArr = mergeSort(leftArr, inver_count).returnArr;
            rightArr = mergeSort(rightArr, inver_count).returnArr;

            int i = 0; int j = 0; int p = 0;

            //merging process
            while (i < leftArr.length && j < rightArr.length) {
                if (leftArr[i] <= rightArr[j]) {
                    returnArr[p] = leftArr[i];

                    i++;
                }

                else {
                    returnArr[p] = rightArr[j];

                    j++;
                    inver_count += (Math.floorDiv(r, 2)+1)-i;
                }
                p++;
            }


            while (i < leftArr.length) {
                returnArr[p] = leftArr[i];

                i++; p++;
            }


            while (j < rightArr.length) {
                returnArr[p] = rightArr[j];

                j++; p++;
            }

            //sorted array is index 0, inver count is index 1
            returnTwo res = new returnTwo(returnArr, inver_count);

            return res;
        }
        returnTwo res = new returnTwo(arr, inver_count);

        return res;
        
    }

}
