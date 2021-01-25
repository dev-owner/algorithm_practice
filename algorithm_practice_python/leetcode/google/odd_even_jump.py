from typing import List


class OddEvenJump:
    def oddEvenJumps(self, A: List[int]) -> int:
        """
        odd jump, even jump가 있고 index i부터 j까지 (i<j) 이동해야 함
        odd jump는 index j 까지 A[i] <= A[j] 이면서 A[j]가 가장 작은 값으로 점프 가능. j 대상이 여러개면 가장 작은 j.
        even jump는 index j 까지 A[i] >= A[j] 이면서 A[j]가 가장 큰 값으로 점프 가능. j 대상이 여러개면 가장 작은 j.
        특정 i는 점프를 못할 수도 있음.

        좋은 출발 index는 해당 index에서 출발 했을 때, 배열의 끝에 도달할 수 있어야 함. (0번 이상 점프하여)
        좋은 스타팅 인덱스의 갯수를 반환해라.
        """

        n = len(A)
        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True

        sorted_idx = sorted(range(n), key=lambda i: A[i])
        odd_next_bucket = OddEvenJump.get_next_hops(sorted_idx)
        sorted_idx.sort(key=lambda i: -A[i])
        even_next_bucket = OddEvenJump.get_next_hops(sorted_idx)

        for i in reversed(range(n - 1)):
            odd_next, even_next = odd_next_bucket[i], even_next_bucket[i]

            if odd_next:
                odd[i] = even[odd_next]
            if even_next:
                even[i] = odd[even_next]

        return sum(odd)

    @classmethod
    def get_next_hops(cls, idxs_sorted_by_value):
        """
        monotonic stack.
        이미 값으로 정렬된 인덱스를 받아, 해당 인덱스보다 큰 제일 첫번째 인덱스를 next_hop에 저장하여 next_hop 배열을 반환
        """
        next_hop = [None] * len(idxs_sorted_by_value)
        stack = []

        for i in idxs_sorted_by_value:
            while stack and stack[-1] < i:
                next_hop[stack.pop()] = i
            stack.append(i)

        return next_hop
