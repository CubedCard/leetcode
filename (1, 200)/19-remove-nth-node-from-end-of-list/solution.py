# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        current = head
        if length == 1:
            return None
        if length == n:
            return head.next
        for _ in range(length - n - 1):
            current = current.next
        current.next = current.next.next

        return head
