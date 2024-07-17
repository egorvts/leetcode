# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 and (list1.next == None) and (list2.next == None):
            a, b = list1.val, list2.val
            return ListNode(min(a, b), ListNode(max(a, b), None))