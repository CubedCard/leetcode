class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        node1 = head
        node2 = head.next
        if not node2:
            return node1
        node1.next = node2.next
        node2.next = node1
        head = node2
        node1.next = self.swapPairs(node1.next)

        return head
