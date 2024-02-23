class Solution {
    public int maximum69Number (int num) {
        int a = num;
        for (int i = 0; i < String.valueOf(num).length(); i++) {
            StringBuilder max = new StringBuilder(String.valueOf(num));
            if (max.charAt(i) == '6') {
                max.setCharAt(i, '9');
            } else if (max.charAt(i) == '9') {
                max.setCharAt(i, '6');
            }
            if (Integer.parseInt(max.toString()) > a) {
                a = Integer.parseInt(max.toString());
            }
        }
        return a;
    }
}
