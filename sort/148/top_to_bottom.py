# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortfun(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortfun(head, mid), sortfun(mid, tail))
            
        def merge(head, tail):
            dummyhead = ListNode(0)
            temp, temp2, temp3 = dummyhead, head, tail
            while temp2 and temp3:
                if temp2.val < temp3.val:
                    temp.next = temp2
                    temp2 = temp2.next
                else:
                    temp.next = temp3
                    temp3 = temp3.next
                temp = temp.next
            if temp2:
                temp.next = temp2
            elif temp3:
                temp.next = temp3
            
            return dummyhead.next

        return sortfun(head, None)

                    
