public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int min = 0;
        int max = nums.Count() - 1;

        if (max == -1)
            return [-1,-1];

        while (min <= max) {
            int mid = min + (max - min) / 2;

            if (nums[mid] == target)
                return FindBeforeAndAfter(nums, mid, target);

            if (nums[mid] < target)
                min = mid + 1;
            else 
                max = mid - 1;
        }

        return [-1,-1];
    }

    private int[] FindBeforeAndAfter(int[] nums, int mid, int target)
    {
        int before = 0;
        int after = 0;

        for (int i = mid + 1; i < nums.Count(); i++)
        {
            if (nums[i] == target)
                after += 1;
            else
                break;
        }

        for (int i = mid - 1; i >= 0; i--)
        {
            if (nums[i] == target)
                before += 1;
            else
                break;
        }

        return [mid - before,mid + after];
    }
}
