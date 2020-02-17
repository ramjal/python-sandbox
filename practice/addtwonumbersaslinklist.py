# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getTheValue(self, l):
        i = 0
        keep = 0
        while l:
            keep = keep + l.val * (10 ** i)
            i += 1
            l = l.next
        return keep
    
    def addTwoNumbers(self, l1, l2, c = 0):
        total = self.getTheValue(l1) + self.getTheValue(l2)
        ll = []
        while total > 0:
            ll.append(total % 10)
            total = int(total / 10)          
        print(ll)        

        tip = ListNode(ll[0])
        l3 = tip
        for d in ll[1:]:
            l3.next = ListNode(d)
            l3 = l3.next
        return tip


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next


# 7 
# 0 
# 8