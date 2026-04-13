public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        Array.Sort(arr);

        int diff = arr[1] - arr[0];

        for (int i = 0; i < arr.Count() - 1; i++)
        {
            if (arr[i] + diff != arr[i + 1])
                return false;
        }

        return true;
    }
}
