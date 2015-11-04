# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        l=head
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                p=ListNode(l1.val)
                l.next=p
                l=l.next
                l1=l1.next
            else:
                p=ListNode(l2.val)
                l.next=p
                l=l.next
                l2=l2.next
        while l1!=None:
            p=ListNode(l1.val)
            l.next=p
            l=l.next
            l1=l1.next
        while l2!=None:
            p=ListNode(l2.val)
            l.next=p
            l=l.next
            l2=l2.next
            print(l.val)
        l.next=None
        return head.next
