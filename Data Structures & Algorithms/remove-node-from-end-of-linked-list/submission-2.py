# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        target = length - n
        print(length)
        print(target)
        
        count = 0

        curr = head
        prev = None
        while curr:
            if count == target:
                if target == 0:
                    return head.next
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            count += 1

        
        return head
            
