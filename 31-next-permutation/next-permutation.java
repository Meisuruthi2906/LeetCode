class Solution {
    public void reverse(int nums[], int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    public void swap(int nums[], int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;
        // Step 1: Find the first decreasing element from the right
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        
        if (i >= 0) {
            int j = n - 1;
            // Step 2: Find the number just larger than nums[i]
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        
        // Step 3: Reverse the suffix to get the smallest possible tail
        reverse(nums, i + 1);
    }
}