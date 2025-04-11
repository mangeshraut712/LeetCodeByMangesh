class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        
        prev_group_tail = dummy
        
        while True:
            # 1. Find the k-th node
            kth_node = prev_group_tail
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            # 2. Store pointers
            next_group_head = kth_node.next
            group_head = prev_group_tail.next
            
            # 3. Reverse the k-group
            prev = next_group_head
            curr = group_head
            while curr != next_group_head:
                temp_next = curr.next
                curr.next = prev
                prev = curr
                curr = temp_next
                
            # 4. Connect the reversed group
            new_head_of_reversed_group = prev 
            new_tail_of_reversed_group = group_head
            
            prev_group_tail.next = new_head_of_reversed_group
            new_tail_of_reversed_group.next = next_group_head
            
            # 5. Update prev_group_tail for the next iteration
            prev_group_tail = new_tail_of_reversed_group