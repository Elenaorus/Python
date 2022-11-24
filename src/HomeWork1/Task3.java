package HomeWork1;

public class Task3 {
}

class Solution3 {
    public int removeElement(int[] nums, int val) {
        int count = 0;

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] != val) {
                nums[count++] = nums[i];
            }
        }
        return count;

    }
}