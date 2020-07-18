# You are given two non-empty linked lists representing two non-negative integer
# s. The digits are stored in reverse order and each of their nodes contain a sing
# le digit. Add the two numbers and return it as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  Example: 
# 
#  
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#  
#  Related Topics Linked List Math 
#  👍 8458 👎 2145

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        res = root
        add_one = 0
        while l1 and l2:
            temp_sum = l1.val + l2.val + add_one
            if temp_sum >= 10:
                add_one = 1
                temp_sum -= 10
            else:
                add_one = 0
            res.next = ListNode(temp_sum)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            res.next = l1
        else:
            res.next = l2
        while add_one == 1:
            if res.next:
                if res.next.val == 9:
                    res.next.val = 0
                    res = res.next
                else:
                    res.next.val += 1
                    add_one = 0
            else:
                res.next = ListNode(1)
                add_one = 0
        return root.next
        
# leetcode submit region end(Prohibit modification and deletion)

