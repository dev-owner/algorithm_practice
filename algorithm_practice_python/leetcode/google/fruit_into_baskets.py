from typing import List


class FruitIntoBaskets:
    def totalFruit(self, tree: List[int]) -> int:
        """
        tree에서 i번째 줄 과일을 tree[i] type이라고 하자.
        선택에 따라 tree 어느곳에서든 시작해서 아래 룰을 따르자.
        1. baskets에 과일 하나 넣고, 만약 못한다면 멈춘다.
        2. 현재 tree 기준 오른쪽 tree로 이동한다. 만약 tree가 없다면 멈춘다.
        한번 스타팅 정하면 변경 불가하고 멈출때까지 1,2번 반복
        너는 2개 baskets이 있고, 무제한이지만 한 basket에는 하나의 종류만 담을 수 있다.
        이 방식대로 모을 수 있는 과일의 최대 수는?
        = 하나의 리스트에서 2개 값이 최대한 많이 붙어 있는 길이는?
        = 리스트에서 2개의 type으로만 이루어져 있는 가장 긴 subset의 길이를 구하면?
        :param tree:
        :return:
        """

        res = cur = a = b = window_size = 0

        for c in tree:
            """
            a,b는 서로다른 마지막 과일
            마지막 type의 갯수를 유지하면서 계속 진행하면 된다.
            time:O(N), space:O(1)
            """

            cur = cur + 1 if c in (a, b) else window_size + 1
            window_size = window_size + 1 if c == b else 1

            if c != b:
                a, b = b, c

            res = max(res, cur)

        return res
