class Solution:
    def countOfAtoms(self, formula: str) -> str:
        #先处理一下字符串，把各个元素，倍数区分出来，比如Mg放到一个位置，11放到一个位置
        #注意把没有数字的后面补上1
        forList=[]
        #for i in range(len(formula)):
        i=0
        while i<len(formula):
            if formula[i]=="(" :
                forList.append(formula[i])
            elif formula[i]==")":
                forList.append(formula[i])
                if i>=len(formula)-1 or not formula[i+1].isdigit():
                    #有可能右括号后面没数字
                    forList.append(1)
            elif formula[i].isdigit():
                start = i
                end =i+1
                while end<len(formula) and formula[end].isdigit():
                    end+=1
                    i+=1
                multi = int(formula[start:end])
                forList.append(multi)
            elif formula[i].islower():continue
            else:
                #字母
                start = i
                end = i+1
                while end<len(formula) and formula[end].islower():
                    end+=1
                    i+=1
                forList.append(formula[start:end])
                if i==len(formula)-1 or (i<len(formula)-1 and not formula[i+1].isdigit()):
                    forList.append(1)
            i += 1
        lB=[]
        #将右括号后面的数字，放到字母后面，然后改为一个可以识别且去掉的元素
        for i in range(len(forList)):
            if forList[i]=="(":
                lB.append(i)
            elif forList[i]==")":
                mul = forList[i+1]
                forList[i+1]="-"
                startIndex = lB.pop()+1
                for l in range(startIndex,i):
                    if forList[i]=="-" or forList[l]=="(" or forList[l]==")":continue
                    if isinstance(forList[l],str) and forList[l].isalpha():
                        forList[l+1] *=mul
        seq=[]
        dic ={}
        for i in range(len(forList)):
            if forList[i]=="-" or forList[i]=="(" or forList[i]==")" or isinstance(forList[i],int):
                continue
            if forList[i] not in seq:
                seq.append(forList[i])
            if dic.get(forList[i]):
                dic[forList[i]] = dic[forList[i]]+forList[i+1]
            else:
                dic[forList[i]] = forList[i + 1]
        ans=""
        seq.sort()
        for letter in seq:
            if dic[letter]>1:
                ans+=letter+str(dic[letter])
            else:
                ans += letter
        return ans







'''
726. Number of Atoms
Hard
Given a string formula representing a chemical formula, return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.
For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.
Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
'''