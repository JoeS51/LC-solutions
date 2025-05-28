class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        res = []
        while curr and size > 0:
            curr_seg = ceil(size / k)
            size -= curr_seg
            temp_head = ListNode(val=curr.val) 
            h = temp_head
            while curr and curr_seg > 1:
                curr = curr.next
                temp_head.next = ListNode(curr.val)
                temp_head = temp_head.next 
                curr_seg -= 1
            if temp_head:
                temp_head.next = None
                curr = curr.next
            res.append(h)
            k -= 1
        while k > 0:
            res.append(None)
            k -= 1
        return res

