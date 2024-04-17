# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        pointer = answer
        print(pointer)
        # print(l1)
        # >>> ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
        residual = 0
        while l1 or l2 or residual:
            node = 0
            if l1:
                node += l1.val
                l1 = l1.next
            if l2:
                node += l2.val
                l2 = l2.next

            node += residual
            if node >= 10:
                pointer.next = ListNode(node%10)
                pointer = pointer.next
                residual = 1
            else:
                pointer.next = ListNode(node)
                pointer = pointer.next
                residual = 0
            
        return answer.next