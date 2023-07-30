class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children=[None]*26
            self.isWord=False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        Node=self.root
        for ch in word:
            index = ord(ch)-ord("a")
            if not Node.children[index]:
                Node.children[index]=self.TrieNode()
            Node =Node.children[index]
        Node.isWord=True

    def search(self, word: str) -> bool:
        '''
        这个逻辑不行，会导致只要点超过实际单词长度，匹配到一个就能返回true
        #find the number of '.' in the end, then reduce the recursion time
        n = 0
        for i in range(len(word)-1,-1,-1):
            if word[i]=='.':
                n+=1
            else:
                break
        self.radomNum = n
        '''
        
        return self.find(word,self.root,0)

    def find(self,word,node,wordIndex):
        if node==None:return False
        if not word:return False
        if wordIndex == len(word):return node.isWord
        cur = word[wordIndex]
        if cur=='.':
            '''
            这个逻辑不行，会导致只要点超过实际单词长度，匹配到一个就能返回true
            if self.radomNum+wordIndex==len(word):
                #发生在'.'出现在最后，所以只要看字符个数，不用再去扫描了
                return True
            '''
            for trieNd in node.children:
                if self.find(word,trieNd,wordIndex+1):
                    return True
        else:
            arrIndex=ord(cur)-ord('a')
            tempNode = node.children[arrIndex]
            return self.find(word,tempNode,wordIndex+1)




        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



'''
211. Design Add and Search Words Data Structure
Medium
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.'''