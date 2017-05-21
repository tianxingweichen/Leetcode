# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next==None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p2 = head
        while p2.next != None:
            if p2.val > p2.next.val:
                p1 = dummy
                while p2.next.val>p1.next.val:
                    p1 = p1.next
                t = p2.next
                p2.next = p2.next.next
                t.next = p1.next
                p1.next = t
            else:
                p2 = p2.next
        return dummy.next


