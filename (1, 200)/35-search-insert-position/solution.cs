public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int min = 0;
        int max = nums.Count() - 1;
        while (min <= max) {
            int mid = min + (max - min) / 2;

            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target)
                min = mid + 1;
            else
                max = mid - 1;
        }
        return min;
    }
}
