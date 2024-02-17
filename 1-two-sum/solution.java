class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (2 > nums.length || nums.length > 10E4) {
            return null;
        }
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}
