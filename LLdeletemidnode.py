# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=ListNode(0,head)
        slow,fast=head1,head1
        while fast and fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return head1.next
        
