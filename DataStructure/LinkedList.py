"""
name: LinkedList
author : jimi
date : 2019/12/25
"""

"""单链表结点"""


class linknode():
    def __init__(self,val):
        self.val = val
        self.next = None


"""单链表"""


class SingleLinkedList():
    """初始化链表"""
    def __init__(self,t:list):
        assert t,'列表不能为空'
        assert isinstance(t,list),'传入的结构必须是列表'
        head = linknode(t[0])
        t.pop(0)
        p = head
        while t:
            val = t.pop(0)
            p.next = linknode(val)
            p = p.next
        self.linklist = head
        print(self.showlinkedlist(self.linklist))

    """可视化链表"""
    def showlinkedlist(self,head):
        showlist = ['head']
        while head != None:
            showlist.append(head.val)
            if head.next != None:
                showlist.append('-->')
            else:
                showlist.append(('tail'))
            head = head.next
        return showlist

    """三指针法反转单链表"""
    def reverse(self,head):
        pre = head
        cur = head.next
        if cur:
            nxt = cur.next
        else:
            nxt = None
        while cur or nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        head.next = None  # 转完以后要把原来的初始指针的next 设为None
        head = pre  # 再将pre指针所指向的原链表的结尾指针，赋给头指针
        return head

    """快慢指针法 找到链表的中心位置,偶数个的中心位置取上整"""
    def findcenter(self,head):  # head为链表的头指针
        n = 0
        left = head
        right = None
        if left.next:
            right = head.next
        while right and right.next:
            left = left.next
            right = right.next.next
            n += 1
        if right and not right.next:
            left = left.next
            n += 1
        middle = left
        return middle # n为middle的位置序号 从0开始记数

    """高效查找单链表是否为回文链表"""
    def ispalindroom(self):
        head = self.linklist

        """找到中心位置"""
        mid = self.findcenter(head)

        """中心往右的链表，反转,将中心结点的next设置为None"""
        right = self.reverse(mid)
        root_r = right
        """小小的可视化一下"""
        print("left:",self.showlinkedlist(head))
        print("right",self.showlinkedlist(right))

        """两个链表，双指针判断是否回文"""
        flag = True
        left  = head
        while left and right:
            if left.val != right.val:
                flag = False
                break
            left = left.next
            right = right.next
        """将原链表还原"""
        self.reverse(root_r) #  翻转回来
        print(self.showlinkedlist(self.linklist))
        return flag

if __name__ == "__main__":
    linklist = [1,2,1]
    a=SingleLinkedList(linklist)
    print(a.ispalindroom())

