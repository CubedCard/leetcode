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
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        if (head != null) {
            ListNode next = head.next;
        
            current.next = null;
         
            while(next != null) {
              ListNode temp = next.next;
              next.next = current;
               current = next;
              next = temp;
            }
        }
        return current;
    }
}
