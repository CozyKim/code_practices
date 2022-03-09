# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self) -> None:
        self.word = False
        self.chiledren = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.chiledren:
                node.chiledren[char] = TrieNode()
            node = node.chiledren[char]
        node.word = True  # 단어가 모두 완성 되었을 때를 의미한다.

    # 찾으려는 단어가 존재하는지 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.chiledren:
                return False
            node = node.chiledren[char]

        return node.word  # 만약 완선된 트라이라면 True로 될 것이고 아니면 False로 나올 것이다

    # 해당 문자열로 시작하는 단어가 존재하는지 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.chiledren:
                return False
            node = node.chiledren[char]

        return True
