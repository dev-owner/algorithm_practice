from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        기존에 알파벳은 고유의 ascii code가 있는데 이걸 바꿀 방법이?
        새로 mapping table 만들고 sort key를 바꾼다.
        :param words: 주어진 외계인 단어
        :param order: 외계인 알파벳 순서
        :return: 주어진 order에 맞게 words가 알파벳 순으로 정렬되어 있는가?
        """

        new_ascii_map = {alphabet: idx for idx, alphabet in enumerate(list(order))}

        class AlienOrder:
            def __init__(self, inner):
                self.inner = inner

            def __lt__(self, other):
                for i in range(min(len(self.inner), len(other.inner))):
                    a = new_ascii_map.get(self.inner[i])
                    b = new_ascii_map.get(other.inner[i])
                    if a != b:
                        return a < b
                return len(self.inner) < len(other.inner)

        sorted_list = sorted(words, key=AlienOrder)

        return words == sorted_list
