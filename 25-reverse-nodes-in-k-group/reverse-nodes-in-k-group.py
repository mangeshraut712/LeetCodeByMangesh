class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        
        while True:
            kth_node = prev_group_tail
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            next_group_head = kth_node.next
            group_head = prev_group_tail.next
            
            prev = next_group_head
            curr = group_head
            while curr != next_group_head:
                temp_next = curr.next
                curr.next = prev
                prev = curr
                curr = temp_next
                
            prev_group_tail.next = prev
            group_head.next = next_group_head
            prev_group_tail = group_head