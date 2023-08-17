class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans=[]
        n,i = len(words),0
        #确定每一行最多多少个单词
        while i <n:
            j=i 
            count=0
            while j<n:
                if j==i:
                    count+=len(words[j])
                else:
                    count+=1+len(words[j])
                if count>maxWidth:break
                j+=1
            j-=1
            if j==n-1 or i==j:
                #最后一组或者这一行只有一个单词
                strs=words[i]
                for x in range(i+1,j+1):
                    strs+=" "+words[x]
                strs+=" "*(maxWidth-len(strs))
                ans.append(strs)
            else:
                ans.append(self.putWords(i,j,words,maxWidth))
            i=j+1
        return ans

    def putWords(self,start,end,wordsList,maxWidth):
        count=0
        for i in range(start,end):
            count+=len(wordsList[i])+1
            wordsList[i]+=" "
        count+=len(wordsList[end])
        #需要补齐的空格数
        left = maxWidth-count
        gapNum = end-start
        if left//gapNum>0:
            #说明空格足够每个间隙加至少1个，
            num = left//gapNum
            for i in range(start,end):
                wordsList[i]+=" "*num
            left=left%gapNum
        if left and left<gapNum:
            #不足一轮，每个+1就好
            i=start
            while i<end and left>0:
                wordsList[i]+=" "
                left-=1
                i+=1

        return "".join(wordsList[start:end+1])
'''
68. Text Justification
Hard
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth'''