# build a tree like:
#             "d"
#     "do"            "da"
# "dog"  "dom"    "dar"    "dat"
#
# so we can optimize startsWith predicate and easily insert/search
#
# hint 1 & 2 given, the tree's nodes are one char with a list of children instead

class TreeNode:

    def __init__(self, val: str, end = False):
        self.val = val
        self.end = end
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TreeNode(None)
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            isEnd = i == len(word) - 1

            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = TreeNode(c, isEnd)

            node = node.children[ord(c) - ord('a')]

            if isEnd and not node.end: node.end = True
            


    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            isEnd = i == len(word) - 1

            if not node.children[ord(c) - ord('a')]:
                return False

            node = node.children[ord(c) - ord('a')]

            if isEnd and not node.end: return False

        return True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            c = prefix[i]

            if not node.children[ord(c) - ord('a')]:
                return False

            node = node.children[ord(c) - ord('a')]

        return True
    
        