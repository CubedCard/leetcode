public class Solution {
    public bool IsUgly(int n) {
        if (n <= 0)
            return false;
        if (n < 7 && (n % 2 == 0 || n % 3 == 0 || n % 5 == 0))
            return true;
        if (n % 2 != 0)
            return false;
        
        int x = n / 2;
        return x % 2 == 0 || x % 3 == 0 || x % 5 == 0;
    }
}
