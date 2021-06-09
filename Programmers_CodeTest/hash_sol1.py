
# from enum import Enum
# import hashlib
# from typing import runtime_checkable


# def solution(participant, completion):
#     hash = OpenHash(len(participant))
#     for s in participant:
#         hash.add(s, s)
#     for s in completion:
#         hash.remove(s)
#     answer = hash.dump()
#     return answer


# class Status(Enum):
#     OCCUPIED = 0        # 데이터를 저장
#     EMPTY = 1           # 비어 있음
#     DELETED = 2         # 삭제 완료


# class Bucket:
#     """해시를 구성하는 버킷"""

#     def __init__(self, key=None, value=None, stat=Status.EMPTY) -> None:
#         """초기화"""
#         self.key = key      # 키
#         self.value = value  # 값
#         self.stat = stat    # 속성

#     def set(self, key, value,  stat: Status) -> None:
#         """모든 필드에 값을 설정"""
#         self.key = key      # 키
#         self.value = value  # 값
#         self.stat = stat    # 속성

#     def set_status(self, stat: Status) -> None:
#         """속성을 설정"""
#         self.stat = stat


# class OpenHash:
#     """오픈 주소법으로 구현하는 해시 클래스"""

#     def __init__(self, capacity: int) -> None:
#         """초기화"""
#         self.capacity = capacity                    # 해시 테이블의 크기를 지정
#         self.table = [Bucket()] * self.capacity     # 해시 테이블

#     def hash_value(self, key) -> int:
#         """해시값을 구함"""
#         if isinstance(key, int):                    # 자료형 확인하는 함수
#             return key % self.capacity
#         return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

#     def rehash_value(self, key) -> int:
#         """재해시 값을 구함"""
#         return(self.hash_value(key)+1) % self.capacity

#     def search_node(self, key):
#         """키가 key인 버킷을 탐색"""
#         hash = self.hash_value(key)             # 검색하는 키의 해시값
#         p = self.table[hash]                    # 버킷을 주목

#         for i in range(self.capacity):
#             if p.stat == Status.EMPTY:
#                 break
#             elif p.stat == Status.OCCUPIED and p.key == key:
#                 return p
#             hash = self.rehash_value(hash)      # 재해시
#             p = self.table[hash]
#         return None

#     def search(self, key):
#         """키가 key인 원소를 검색하여 값을 반환"""
#         p = self.search_node(key)
#         if p is not None:
#             return p.value                      # 검색 성공
#         else:
#             return None                         # 검색 실패

#     # def add(self, key, value):
#     #     if self.search(key) is not None:
#     #         hash = self.rehash_value(key)
#     #         # 추가 할 것 : 서치해서 이미 있을경우 재 해시해서 다른데 저장하는거 만들기
#     #         p = self.table[hash]
#     #         for i in range(self.capacity):
#     #             if p.stat == Status.EMPTY:
#     #                 break

#     def add(self, key, value) -> bool:
#         """키가 key이고 값이 value인 원소를 추가"""
#         if self.search(key) is not None:
#             hash = self.rehash_value(key)             # 검색하는 키의 해시값
#             p = self.table[hash]
#             for i in range(self.capacity):
#                 if p.stat == Status.EMPTY or p.stat == Status.DELETED:
#                     self.table[hash] = Bucket(key, value, Status.OCCUPIED)
#                     return True
#                 hash = self.rehash_value(hash)      # 재해시
#                 p = self.table[hash]
#             return False                        # 이미 등록된 키
#         hash = self.hash_value(key)             # 추가하는 키의 해시값
#         p = self.table[hash]                    # 버킷을 주목
#         for i in range(self.capacity):
#             if p.stat == Status.EMPTY or p.stat == Status.DELETED:
#                 self.table[hash] = Bucket(key, value, Status.OCCUPIED)
#                 return True
#             hash = self.rehash_value(hash)      # 재해시
#             p = self.table[hash]
#         return False

#     def remove(self, key) -> int:
#         """키가 key인 원소를 삭제"""
#         p = self.search_node(key)               # 버킷을 주목
#         if p is None:
#             return False                        # 이 키는 등록된 것이 아님
#         p.set_status(Status.DELETED)
#         return True

#     def dump(self) -> None:
#         """해시 테이블을 덤프"""
#         for i in range(self.capacity):
#             if self.table[i].stat == Status.OCCUPIED:
#                 return self.table[i].key
import hashlib


class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key, value, next) -> None:
        """초기화"""
        self.key = key      # 키
        self.value = value  # 값
        self.next = next    # 뒤쪽 노드를 참조


class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key):
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]        # 노드를 주목

        while p is not None:
            if p.key == key:        # 검색 성공
                return p.value      # 뒤쪽 노드를 주목
            p = p.next

        return None                 # 검색 실패

    def add(self, key, value) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)  # 추가하려는 key의 해시값
        p = self.table[hash]        # 노드를 주목

        while p is not None:
            # if p.key == key:
            #     return False        # 추가 실패
            p = p.next              # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp     # 노드를 추가
        return True                 # 추가 성공

    def remove(self, key) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)  # 삭제할 key의 해시값
        p = self.table[hash]         # 노드를 주목
        pp = None                   # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True         # key 삭제 성공
            pp = p
            p = p.next              # 뒤쪽 노드를 주목
        return False                # 삭제 실패 (key가 존재하지 않음)

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            if p is not None:
                return p.key


def solution(participant, completion):
    hash = ChainedHash(len(participant))
    for s in participant:
        hash.add(s, s)
    for s in completion:
        hash.remove(s)
    answer = hash.dump()
    return answer


print(solution(	["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
