import java.util.Arrays;

public class countInversions {
    public static void main(String[] args) {
        Integer[] arr = new Integer[]{3, 4, 1, 2,5,7,6};

        System.out.println(Arrays.toString(mergeSort(arr))); 
    }


    public static int mergeAndCountInversions(Integer[] arr) {
        if (arr.length > 1) {
            Integer l = 0;
            Integer r = arr.length-1;

            Integer[] leftArr = Arrays.copyOfRange(arr, l, Math.floorDiv(r, 2)+1);
            Integer[] rightArr = Arrays.copyOfRange(arr, Math.floorDiv(r, 2)+1, r+1);

            int left_inversions = mergeAndCountInversions(leftArr);
            int right_inversions = mergeAndCountInversions(rightArr);
            int split_inversions = mergeAndCountInversions(arr);

            int total_inversions = left_inversions + right_inversions + split_inversions;

            return total_inversions;
        }

        return 0;
    }


    public static Integer[] mergeSort(Integer[] arr) {
        if (arr.length > 1) {
            //variables for simplicity 
            Integer l = 0;
            Integer r = arr.length-1;

            Integer[] returnArr = new Integer[arr.length];
            Integer[] leftArr = Arrays.copyOfRange(arr, l, Math.floorDiv(r, 2)+1);
            Integer[] rightArr = Arrays.copyOfRange(arr, Math.floorDiv(r, 2)+1, r+1);

            //recursive function calls
            leftArr = mergeSort(leftArr);
            rightArr = mergeSort(rightArr);

            int i = 0; int j = 0; int p = 0;

            while (i < leftArr.length && j < rightArr.length) {
                if (rightArr[j] < leftArr[i]) {
                    returnArr[p] = rightArr[j];

                    j++;
                }

                else {
                    returnArr[p] = leftArr[i];

                    i++;
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


            return returnArr;
        }

        return arr;
        
    }
}
