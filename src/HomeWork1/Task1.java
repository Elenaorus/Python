package HomeWork1;
public class Task1 {
}

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = m + n - 1;
        int indexNums1 = m - 1, indexNums2 = n - 1;

        while (indexNums2 >= 0) {
            if (indexNums1 < 0) {
                nums1[index--] = nums2[indexNums2--];
            } else {
                if (nums2[indexNums2] >= nums1[indexNums1]) {
                    nums1[index--] = nums2[indexNums2--];
                } else {
                    nums1[index--] = nums1[indexNums1--];
                }
            }
        }

    }
}