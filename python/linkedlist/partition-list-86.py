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
        smallVals = ListNode(-1, None)
        s_ptr = smallVals
        bigVals = ListNode(-1, None)
        b_ptr = bigVals
        while head != None:
            curr_node = ListNode(head.val, None)
            if head.val < x:
                s_ptr.next = curr_node
                s_ptr = s_ptr.next
            else:
                b_ptr.next = curr_node
                b_ptr = b_ptr.next
            head = head.next
        s_ptr.next = bigVals.next
        return smallVals.next

# Linked list problem that uses a clever solution of just having two separate lists: one list storing values less than x and one list storing values greater than or equal to x. This preserves the ordering and allows you to combine them at the end for the solution

# runtime: O(n)
# Spacetime: O(1) because they're just pointers
