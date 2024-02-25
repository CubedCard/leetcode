class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            smallest = cur1 if cur1.val < cur2.val else cur2
            biggest = cur1 if cur1.val >= cur2.val else cur2

            cur1 = smallest.next
            cur2 = biggest

            if smallest.next:
                smallest.next = cur1 if cur1.val < cur2.val else cur2
            else:
                smallest.next = cur2
        
        if not list1:
            return list2
        if not list2:
            return list1
        return list1 if list1.val < list2.val else list2
