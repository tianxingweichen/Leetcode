# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解题思路:快慢指针与归并排序
# 首先用快慢指针方法找出链表的中间位置，将链表分成两个部分，
# 然后通过归并排序的方法分别对这个部分进行排序再合并，最终得到顺序序列。

# 快慢指针：让快慢指针从链表头开始遍历，快指针向前移动两个位置，
# 慢指针向前移动一个位置，当快指针到达链表尾时，慢指针到达中点。

# 归并排序：将数组分成两组A,B,再将A,B组各自分成两组，依次类推，当分出来的小组只有一个数时，
# 可以认为这是有序的，然后再合并相邻的两个小组。这样通过先递归的分解数列，再合并数列就完成了归并排序
class Solution(object):
    def sortList(self, head):
        if head == None or head.next==None:
            return head
        slow = ListNode(0)
        slow.next = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        tmp1 = self.sortList(head1)
        tmp2 = self.sortList(head2)
        ans = ListNode(0)
        p = ans
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                p.next = tmp1
                tmp1, p = tmp1.next, p.next
            else:
                p.next = tmp2
                tmp2, p = tmp2.next, p.next
        if tmp1:
            p.next = tmp1
        if tmp2:
            p.next =tmp2
        return ans.next
