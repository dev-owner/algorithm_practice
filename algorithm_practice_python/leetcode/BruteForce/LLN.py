class LLN:
    @staticmethod
    def run(n=0, m=0, k=0, N=""):
        # N, M, K 공백 구분 입력
        if not (n and m and k):
            n, m, k = map(int, input().split())
        # N개의 수를 공백으로 구분하여 입력
        if not N:
            data = list(map(int, input().split()))
        else:
            data = list(map(int, N.split()))

        data.sort()
        first = data[n - 1]
        second = data[n - 2]

        result = 0

        while True:
            for i in range(k):  # 가장 큰 수를 K번 더하기
                if m == 0:
                    break
                result += first
                m -= 1
            if m == 0:
                break
            result += second
            m -= 1
        return result


if __name__ == '__main__':
    print(LLN.run())
