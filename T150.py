class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        #从左到右两个数字后面必然有一个操作符，所以先把数字入栈，遇到操作符，计算，然后结果继续入栈
        operand = []
        for item in tokens:
            if self.isOperator(item):
                n2 = operand.pop()
                n1 = operand.pop()
                res = self.cal(n1,item,n2)
                operand.append(res)
            else:
                operand.append(int(item))
        return operand.pop()

    def isOperator(self,item):
        return (item =="+" or item =="-" or item =="*" or item =="/")
    def cal(self,n1,operator,n2):
        if operator=="+":
            return n1+n2
        elif operator=="-":
            return n1-n2
        elif operator == "/":
            return int(n1/n2)
        else :
            return n1*n2


'''
150. Evaluate Reverse Polish Notation
Medium
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''