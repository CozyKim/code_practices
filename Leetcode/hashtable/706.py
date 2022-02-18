# https://leetcode.com/problems/design-hashmap/

import collections


# 풀이1 : 개별 체이닝 방식을 이용한 해시 테이블 구현


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # 해당 인덱스가 비워져 있다면 바로 연결 리스트를 넣어준다.
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스가 차있다면 체이닝 방식으로 연결 리스트 마지막으로 가서 끝에 붙여준다.
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size

        # 해당 인덱스가 비워져 있다면 오류 : -1
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        # 해시 값에서 키를 찾아 보았는데 발견하지 못하면 오류 : -1
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        # 해당 인덱스가 비워져 있다면 오류 : -1
        if self.table[index].value is None:
            return

        p = self.table[index]

        # 인덱스의 첫 번째 노드가일 때 삭제처리
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


class ListNode:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
