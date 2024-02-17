import java.math.BigInteger;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        String values_l1 = "";
        String values_l2 = "";
        while (l1 != null) {
            values_l1 += (String.valueOf(l1.val));
            l1 = l1.next;
        }

        while (l2 != null) {
            values_l2 += (String.valueOf(l2.val));
            l2 = l2.next;
        }

        String reversed_l1 = new StringBuilder(values_l1).reverse().toString();
        String reversed_l2 = new StringBuilder(values_l2).reverse().toString();

        String sum = String.valueOf(new BigInteger(reversed_l1).add(new BigInteger(reversed_l2)));
        int[] numbers = sum.chars().map(Character::getNumericValue).toArray();

        ListNode result = new ListNode();
        ListNode next = result;
        for (int i = numbers.length - 1; i >= 0; i--) {
            next.val = numbers[i];
            if (i > 0) {
                next.next = new ListNode();
            }
            next = next.next;
        }

        return result;
    }
}
