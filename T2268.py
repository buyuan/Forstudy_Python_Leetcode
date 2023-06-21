import collections


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        #尽量把最高频的放在第一个字母中，需要按一次，第一个字母的用完了，就放在第二个字母中，需要按两次，再不够就放在第三个字母中，需要按三次
        #然后再把字符串按照字符的高频到低频排序。
        #那么实际上，题目就变成了，将频率从高到低，放在九宫格中，而不是一个一个按键

        #生成一个字母为key，频次为value的map
        freq = collections.Counter(s)
        
        #将key按照value的大小（字母出现的频次）排序,从大到小
        letters = sorted(freq.keys(),key = lambda x:freq[x],reverse=True)
        res=0
        keyUsed=0
        position=1
        for c in letters:
            #放在position位置，当前字母有几次，就要按几个position次
            res+=position*freq[c]
            keyUsed+=1
            if keyUsed==9:
                #9个健都用完了,position就要往后移动一次
                position+=1
                keyUsed=0
        return res
'''
2268. Minimum Number of Keypresses
Medium
You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:

All 26 lowercase English letters are mapped to.
Each character is mapped to by exactly 1 button.
Each button maps to at most 3 characters.
To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.

Given a string s, return the minimum number of keypresses needed to type s using your keypad.

Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.

 

Example 1:


Input: s = "apple"
Output: 5
Explanation: One optimal way to setup your keypad is shown above.
Type 'a' by pressing button 1 once.
Type 'p' by pressing button 6 once.
Type 'p' by pressing button 6 once.
Type 'l' by pressing button 5 once.
Type 'e' by pressing button 3 once.
A total of 5 button presses are needed, so return 5.
Example 2:


Input: s = "abcdefghijkl"
Output: 15
Explanation: One optimal way to setup your keypad is shown above.
The letters 'a' to 'i' can each be typed by pressing a button once.
Type 'j' by pressing button 1 twice.
Type 'k' by pressing button 2 twice.
Type 'l' by pressing button 3 twice.
A total of 15 button presses are needed, so return 15.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.'''