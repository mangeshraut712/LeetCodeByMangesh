class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Count k nodes
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head
        
        # Reverse the next group recursively
        new_head = self.reverseKGroup(curr, k)
        
        # Reverse current group
        prev = new_head
        curr = head
        for _ in range(k):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        return prev