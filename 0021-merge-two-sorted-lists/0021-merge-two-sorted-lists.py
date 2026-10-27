# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Create a dummy node to act as the starting point of the merged list.
        # This helps avoid special edge cases for the head node.
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists while neither is empty
        while list1 and list2:
            if list1.val <= list2.val:
                # If list1's value is smaller or equal, append it to the merged list
                current.next = list1
                list1 = list1.next
            else:
                # If list2's value is smaller, append it to the merged list
                current.next = list2
                list2 = list2.next
                
            # Move the current pointer forward
            current = current.next
            
        # If one of the lists is not fully traversed, append the rest of it.
        # Since the lists are already sorted, we can just link the remainder.
        current.next = list1 if list1 else list2
        
        # The merged list starts at dummy.next
        return dummy.next