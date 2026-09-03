# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:

            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = total // 10
            unit = total % 10

            current.next = ListNode(unit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
