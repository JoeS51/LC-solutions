# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = 0
        currA = headA
        while currA:
            lenA += 1
            currA = currA.next
        lenB = 0
        currB = headB
        while currB:
            lenB += 1
            currB = currB.next
        
        while lenA > lenB:
            lenA -= 1
            headA = headA.next
        while lenB > lenA:
            lenB -= 1
            headB = headB.next

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

