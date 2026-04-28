# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists)-1)

    def divide(self, lists, left, right):
        if left > right:
            return None
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        l = self.divide(lists, left, mid)
        r = self.divide(lists, mid+1, right)

        return self.conquer(l, r)

    def conquer(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
            if list1:
                curr.next = list1
            else:
                curr.next = list2

        return dummy.next