package HomeWork1;

public class Task2 {
}

class Solution2 {
    public int[] buildArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] * n;
        }
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] + nums[nums[i] / n] / n;
        }
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] % n;
        }
        return nums;
    }
}