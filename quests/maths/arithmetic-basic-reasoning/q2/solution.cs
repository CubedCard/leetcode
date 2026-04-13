public class Solution {
    public int PivotInteger(int n) {
        int[] arr = Enumerable.Range(1, n).ToArray();

        if (n == 1)
            return 1;

        for (int p = 1; p < n; p++)
        {
            int left = arr.Take(p + 1).Sum();
            int right = arr.Skip(p).Sum();
            if (left == right)
                return p + 1;
        }

        return -1;
    }
}
