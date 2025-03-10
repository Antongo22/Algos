from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse = None

        while slow:
            tmp = slow
            slow = slow.next
            tmp.next = reverse
            reverse = tmp

        while reverse and head:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True
