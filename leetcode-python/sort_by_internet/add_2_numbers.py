# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None
class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print (' value: ', node.val)
            node = node.next

    # def _reverse(self, nodelist):
    #     list = []
    #     while nodelist:
    #         list.append(nodelist.val)
    #         nodelist = nodelist.next
    #     result = ListNode()
    #     result_handle = ListNode_handle()
    #     for i in list:
    #         result = result_handle.add(i)
    #     return result
class Solution():
    def add2numbers(l1,l2):
        ans = ListNode()
        tmp = ans
        tmpsum = 0
        while True:
            if l1 != None:
                tmpsum += l1.val
                l1 = l1.next
            if l2 != None:
                tmpsum += l2.val
                l2 = l2.next
            tmp.val = tmpsum % 10
            tmpsum //=10
            if l1 == None and l2 == None and tmpsum == 0:
                break
            tmp.next = ListNode()
            tmp = tmp.next
        return ans

ListNode_1 = ListNode_handle()
ListNode_2 = ListNode_handle()
l1 = ListNode()
l2 = ListNode()
l1_list = [2,4,3]
l2_list = [5,6,4]
for i in l1_list:
    l1 = ListNode_1.add(i)
for j in l2_list:
    l2 = ListNode_2.add(j)

#ListNode_1.print_ListNode(l2)
ansc = Solution.add2numbers(l1,l2)
ListNode_1.print_ListNode(ansc)

#print(Solution.add2numbers())