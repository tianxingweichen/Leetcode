# 解题思路:快慢指针与逆转指针，链表合并
# 首先用快慢指针方法找出链表的中间位置，将链表分成两个部分，
# 然后将链表后面的部分逆转，最后依次合并两个部分
class Solution(object):
    def rever(self, head):
        pre = None
        while head.next!=None:
            nex = head.next
            head.next = pre
            pre = head
            head = nex 
        head.next = pre
        pre = head
        return pre

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next==None:
            return 
        slow= fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        head1 = head
        head2 = fast
        head2 = self.rever(head2)
        p1 = head1
        p2 = head2
        while p2:
            t1 = p1.next
            p1.next = p2
            t2 = p2.next
            p2.next = t1
            p1 = t1
            p2 = t2