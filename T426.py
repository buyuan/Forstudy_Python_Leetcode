from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #用非递归实现，实际就是栈
    def treeToDoublyList_nonRecur(self, root: Optional[Node]) -> Optional[Node]:
        head, pre=None, None
        stk=[]
        while root or len(stk)>0:
            while root:
                #左子树入站
                stk.append(root)
                root= root.left
            #左，根，因为入栈的规则， 最个一个节点的左子树是None，所以，左相当于遍历过了，现在到了根
            root=stk.pop()
            #处理双链表
            cur = root
            if not head:
                head= cur
                pre = cur
            else:
                pre.right=cur
                cur.left=pre
                pre=cur
            #转向给节点的右子树
            root=root.right
        #链接一头一尾
        head.left=pre
        pre.right=head
        return head

    #这个是递归方法中序遍历
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        #DFS 左根右遍历,加入list，list是排好序的节点，然后用这个list中节点的顺序做双链表
        lst=[]
        self.DFS(lst,root)
        #处理list中的节点
        lst[0].left = lst[-1]
        lst[-1].right = lst[0]
        for i in range(len(lst)-1):
            lst[i+1].left = lst[i]
            lst[i].right=lst[i+1]
        return lst[0]

    def DFS(self, lst,root):
        if not root:
            return
        self.DFS(lst, root.left)
        lst.append(root)
        self.DFS(lst, root.right)

'''
426. Convert Binary Search Tree to Sorted Doubly Linked List
Medium
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
'''