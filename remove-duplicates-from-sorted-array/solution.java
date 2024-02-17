class Solution {
    public int removeDuplicates(int[] nums) {
        int result = nums.length;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] = 101;
                result -= 1;
            }
        }
        Arrays.sort(nums);
        return result;
    }
}
