# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        
        l1_str = ""
        for iteration in l1:
            iteration = str(iteration)
            l1_str += iteration
        l1 = int(l1_str)

        l2_str = ""
        for iteration in l2:
            iteration = str(iteration)
            l2_str += iteration
        l2 = int(l2_str)

        l3 = l1 + l2
        l3 = str(l3)
        l3_list = []
        for iteration in l3:
            l3_list.append(iteration)
        l3_list = l3_list[::-1]

        return l3_list

solution = Solution()
solution.addTwoNumbers([2,4,3], [5,6,4])