import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # 쌍의 합이 60으로 나누어 떨어지는 것들의 인덱스 쌍의 갯수를 반환
        # 모든 쌍의 합을 구하고 조건을 확인 - n^2
        # space는 O(1)
        # 입력 길이가 최대 60000 인걸로 봐서 n^2은 조금 빡세다 36억번 반복 - 10
        cnt = 0
        l = len(time)
        for i in range(0, l):
            for j in range(i + 1, l):
                if (time[i] + time[j]) % 60 == 0:
                    cnt += 1
        return cnt

    def numPairsDivisibleBy60_2(self, time: List[int]) -> int:
        # 쌍의 합이 60으로 나누어 떨어지는 것들의 인덱스 쌍의 갯수를 반환
        # 백트래킹 - 애초에 60으로 절대 나누어 떨어질수 없는 수라면? 근데 더하기때문에 가능성은 있음
        # 정렬하면? 안되고
        # 작은 문제로 나눌수 있을까? 안되고
        # math - (a+b) % 60 == 0 을 찾는데, b가 20이라치면 a는 40 100 160이 pair가 될 수 밖에 없고. 이것들을 60으로 모듈러하면 전부 40
        # 즉 input을 전부 modular 60하고 이전에 (60-x)%60을 만족하는 숫자가 있으면 1씩 더해간다.

        cnt = 0
        seen = [0] * 60
        for t in time:
            idx = (60 - (t % 60)) % 60
            cnt += seen[idx]
            seen[t % 60] += 1

        return cnt

    def numPairsDivisibleBy60_3(self, time: List[int]) -> int:
        # if a % 60 == 0 add remainders
        # time O(n)
        # space O(1)
        remainders = collections.defaultdict(int)
        cnt = 0
        for t in time:
            if t % 60 == 0:
                cnt += remainders[0]
            else:
                cnt += remainders[60-t%60]
            remainders[t % 60] += 1

        return cnt



if __name__ == '__main__':
    time = [30, 20, 150, 100, 40]
    ans = Solution().numPairsDivisibleBy60_3(time)
    print(f'{ans}, 3')
