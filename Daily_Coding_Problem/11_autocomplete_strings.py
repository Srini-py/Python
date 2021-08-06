# Implement an autocomplete system. 
# That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.

class Node:
    def __init__(self, val):
        self.val = val
        self.leaf = False
        self.child = {}


class Trie:
    def __init__(self):
        self.root = {}
        self.final_words = []
      
    def insert(self, string):
        if not self.root:
            self.root[string[0]] = Node(string[0])
        current_node = self.root
        for ch in string[:-1]:
            if (current_node and (ch not in current_node)) or (not current_node):
                    current_node[ch] = Node(ch)
            current_node = current_node[ch].child
        else:
            if (current_node and (string[-1] not in current_node)) or (not current_node):
                    current_node[string[-1]] = Node(string[-1])
            current_node[string[-1]].leaf = True
                        
    def createTrie(self, words):
        for word in words:
            self.insert(word)
            
    def findSuggestions(self, node, word):
        if node[word[-1]].leaf:
            self.final_words.append(word)
        for ch, nd in node.items():
            self.findSuggestions(nd.child, word + ch)
                
    def printSuggestions(self, words, key):
        self.createTrie(words)
        path = self.root
        for ch in key[:-1]:
            if path and (ch not in path) or (not path):
                print("No suggestions found")
                return
            path = path[ch].child
        self.findSuggestions(path, key)
        for i in self.final_words:
            print(i)



words = ['hello', 'dog', 'hell', 'cat', 'a', 'hel', 'help', 'helps', 'helping']
keyword = 'hel'

keywordTrie = Trie()
keywordTrie.printSuggestions(words, keyword)
