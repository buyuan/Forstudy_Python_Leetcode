# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        #用类似leetcode的这个方式序列化
        if not root:
            return '-'
        stk = []
        stk.append(root)
        res = ''
        while stk :
            length = len(stk)
            numFlag = False
            while length>0:
                tmp = stk.pop(0)
                tpStr=""
                if tmp:
                    tpStr+=str(tmp.val)+','
                    numFlag=True
                else:
                    tpStr+='-'+','
                if tmp:
                    stk.append(tmp.left)
                    stk.append(tmp.right)
                length -= 1
            if not numFlag:
                #没有value，不保留这一个字符串,说明也已经是最后一排了
                break
            # 去掉最后一个逗号，以及分行
            tpStr = tpStr[:-1]+'/'
            res+=tpStr
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data =='-':
            return None
        lst = data.split('/')
        root = TreeNode(int(lst[0]))
        cursor = root
        stk=[]
        #上一排的节点
        stk.append(cursor)
        for i in range(1,len(lst)):
            #下一排的节点的val
            cur = lst[i].split(',')
            #上一排节点
            length = len(stk)
            index=0
            while length>0:
                tmpNd = stk.pop(0)
                valLeft = cur[index]
                if valLeft =='-':
                    tmpNd.left = None
                else:
                    nd = TreeNode(valLeft)
                    tmpNd.left = nd
                    stk.append(nd)
                index+=1
                valRight = cur[index]
                if valRight =='-':
                    tmpNd.right = None
                else:
                    nd = TreeNode(valRight)
                    tmpNd.right = nd
                    stk.append(nd)
                index += 1
                length-=1
        return root








# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

'''
297. Serialize and Deserialize Binary Tree
Hard
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''