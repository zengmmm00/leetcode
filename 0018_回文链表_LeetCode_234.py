# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = None
flag = True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global a
        a = head
        global flag
        flag = True
        p = head
        self.recursion(p)
        return flag

    def recursion(self, p):
        global flag
        global a

        if p is None:
            return
        else:
            self.recursion(p.next)
            if a.val != p.val:
                flag = False
            a = a.next
            return


'''
class Solution只新建一个object，会用同一个object跑很多次isPalindrome()，所以要在isPalindrome()中更新全局变量flag = True
'''