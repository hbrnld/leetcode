# https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=leetcode-75

class TrieNode:
    def __init__(self):
        self.children = [None] * 26     # Array to store links to child nodes
        self.isWord = False             # Flag to indicate if the node represents the end of a word

class Trie(object):
    def __init__(self):
        """
        Initialize the data structure.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie.
        """
        curr = self.root

        for c in word: 
            idx = ord(c) - ord("a")                 # Compute index [0, 25]
            if curr.children[idx] == None:          # Add node if empty
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]               # Move to the next node
        curr.isWord = True                          # Mark last node as end of inserted word

    def search(self, word):
        """
        Returns true if the word is in the trie.
        """
        curr = self.root
        for c in word: 
            idx = ord(c) - ord("a")
            if curr.children[idx] == None: 
                return False
            curr = curr.children[idx]
        
        return curr.isWord

    def startsWith(self, prefix):
        """
        Returns true if any word in the trie starts with given prefix.
        """
        curr = self.root

        for c in prefix:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None: 
                return False
            curr = curr.children[idx]
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)