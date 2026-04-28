# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for arr in lists:
            curr = arr
            while curr:
                heap.append(curr.val)
                curr = curr.next
        heapq.heapify(heap)

        if len(heap) == 0: return None
        head = ListNode(heapq.heappop(heap), None)
        for i in range(len(heap)):
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(heapq.heappop(heap), None)
        return head
