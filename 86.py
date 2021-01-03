'''
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

 

示例：

输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyhead = ListNode(0)
        dummyhead.next = head
        pre = dummyhead
        temp = []
        while head:
            if head.val >= x:
                pre = head
                head = head.next
            else:
                pre.next = head.next
                temp.append(head.val)
                head = head.next
        temphead = ListNode(0)
        flow = temphead
        for num in temp:
            listnodetemp = ListNode(num)
            flow.next = listnodetemp
            flow = flow.next
        flow.next = dummyhead.next
        return temphead.next
        
        
