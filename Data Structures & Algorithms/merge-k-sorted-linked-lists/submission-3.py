# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        heap = []
        for arr in lists:
            curr = arr
            while curr:
                heap.append(curr.val)
                curr = curr.next
        heapq.heapify(heap)

        
        
        dummy = ListNode()
        curr = dummy
        for i in range(len(heap)):
            curr.next = ListNode(heapq.heappop(heap), None)
            curr = curr.next

        return dummy.next
