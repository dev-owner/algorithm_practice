from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        1. judge trusts nobody
        2. everybody trusts judge
        3. exactly one person satisfying 1,2

        judge는 [a,b]에서 a에는 있을 수 없고
        모든 사람에 대해 a가 key인 value(list)에 judge가 포함되면 됨

        :param N: number of people
        :param trust: trust[i] = [a,b] representing a trusts b.
        :return: find judge label number
        """
        if N == 1:
            return N

        total = [i for i in range(1, N + 1)]

        cache = {a[0]: list() for a in trust}

        # judge 빼고 key에 다 있어야 함
        if len(cache) != N - 1:
            return -1

        for t in trust:
            cache.get(t[0]).append(t[1])

        for person in total:
            if not cache.get(person):
                for c in cache:
                    if person not in cache.get(c):
                        break
                else:
                    return person
        return -1
