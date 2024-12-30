from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def val(self, ListNode):
        if ListNode is None:
            return float('inf')
        return ListNode.val

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()

        while list1 is not None or list2 is not None:
            if self.val(list1) <= self.val(list2):
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next

        return res.next