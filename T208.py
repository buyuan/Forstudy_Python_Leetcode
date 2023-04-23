import collections


class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            #如果不存在，会自动创建节点并且加入对应的字符的value中
            cur = cur.children[c]
        #到最后一个自然完成了list中的一个单词
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            cur = cur.children.get(c)
            #如果获取到了，则说明存在，获取不到，则说明不存在
            if not cur:return False
        #有可能只是一个中途的部分，不是单词，所以用is_word判断
        return cur.is_word
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if not cur:return False
        return True

class TrieNode:
    def __init__(self):
        #如果key不存在，就自动执行TrieNode（的init），并赋值为这个key的value
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
'''
208. Implement Trie (Prefix Tree)
Medium
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''