import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > 1000) {
            return Double.NaN;
        }
        if (nums2.length > 1000) {
            return Double.NaN;
        }
        if (1 > nums1.length + nums2.length) {
            return Double.NaN;
        }

        int[] merged = Arrays.copyOf(nums1, nums1.length + nums2.length);
        System.arraycopy(nums2, 0, merged, nums1.length, nums2.length);
        
        Arrays.sort(merged);
        
        int mediaanIndex = merged.length / 2;
        
        double mediaan;
        
        if (merged.length % 2 == 0 && mediaanIndex > 0) {
            mediaan = (merged[mediaanIndex] * 1.0 + merged[mediaanIndex - 1]) / 2;
        } else {
            mediaan = merged[mediaanIndex];
        }
        
        return mediaan;
    }
}
