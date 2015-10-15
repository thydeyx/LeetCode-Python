# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre=head
        p1=head
        p=head
        while n!=0:
            n-=1
            p=p.next
        if p==None:
            return p1.next
        p1=p1.next 
        p=p.next
        while p!=None:
            pre=pre.next
            p1=p1.next
            p=p.next
        pre.next=p1.next
        return head
        
        
