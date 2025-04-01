# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        smallPointer = ListNode(-1, None)
        smallPointerHead = smallPointer
        bigPointer = ListNode(-1, None)
        bigPointerHead = bigPointer

        while(head is not None):
            if head.val < x: 
                smallPointer.next = ListNode(head.val, None)
                smallPointer = smallPointer.next
            else:
                bigPointer.next = ListNode(head.val, None)
                bigPointer = bigPointer.next
            head = head.next

        smallPointer.next = bigPointerHead.next
        return smallPointerHead.next

#EX 1: 1432252, X = 3
#Finished: 1222435

#Approach 
#Small List + Big List
# Small List = 1222
# Big List 435

# Iteration 1,2,3,4,5 
