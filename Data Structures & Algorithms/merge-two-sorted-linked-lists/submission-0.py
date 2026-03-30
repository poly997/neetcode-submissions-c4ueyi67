# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = ListNode(-1)

        node = merged_list
        curr_1 = list1
        curr_2 = list2

        while curr_1 and curr_2:

            if curr_1.val >= curr_2.val:
                node.next = curr_2
                curr_2 = curr_2.next
            else:
                node.next = curr_1
                curr_1 = curr_1.next
            node = node.next

        if curr_1 != None:
            node.next = curr_1
        
        if curr_2 != None:
            node.next = curr_2
        
        return merged_list.next

        