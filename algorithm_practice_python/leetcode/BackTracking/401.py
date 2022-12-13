import itertools
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
            H 2^3 2^2 2^1 2^0
            M 2^5 2^4 2^3 2^2 2^1 2^0
            0 <= turnedOn <= 10
        """

        hh = [8, 4, 2, 1]
        mm = [32, 16, 8, 4, 2, 1]

        # combination of hh:mm in turnedOn numbers
        # 2면.. hh에서만 2개씩 모두 mm에서만 2개씩 모두 1개 hh 1개 mm 조합
        # hh는 최대 11까지
        # mm은 최대 60까지
        def get_hh(turnedOn: int):
            ret = []
            if turnedOn == 0: return ["0"]
            for subset in itertools.combinations(hh, turnedOn):
                h = sum(subset)
                if h < 12:
                    ret.append(str(h))
            return ret

        def get_mm(turnedOn: int):
            ret = []
            if turnedOn == 0: return ["00"]
            for subset in itertools.combinations(mm, turnedOn):
                m = sum(subset)
                if m < 60:
                    if m < 10:
                        ret.append(f'0{m}')
                    else:
                        ret.append(str(m))

            return ret

        def get_hh_mm(turnedOn: int):
            ans = []
            for i in range(turnedOn + 1):
                for hhmm in itertools.product(get_hh(i), get_mm(turnedOn - i)):
                    # hhmm = (8, 32) ..
                    ans.append(':'.join(hhmm))
            return ans

        return get_hh_mm(turnedOn)


if __name__ == '__main__':
    turnedOn = 3
    ans = Solution().readBinaryWatch(turnedOn)
    print(len(ans))
    print(f'{ans}, ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]')
