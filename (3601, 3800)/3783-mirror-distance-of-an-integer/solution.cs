public class Solution {
    public int MirrorDistance(int n) {
        char[] c = n.ToString().ToCharArray();
        Array.Reverse(c);
        string r = new string(c);
        int x = int.Parse(r);
        return Math.Abs(n - x);
    }
}
