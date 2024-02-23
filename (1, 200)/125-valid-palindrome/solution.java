class Solution {
    public boolean isPalindrome(String s) {
        String formatted = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String palindrome = new StringBuilder(formatted).reverse().toString();
        return formatted.equals(palindrome);
    }
}
