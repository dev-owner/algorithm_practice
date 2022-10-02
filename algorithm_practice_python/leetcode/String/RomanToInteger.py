class Solution:
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt_prv(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        result = 0
        for c in s:
            result += self.roman_map[c]
        return result

    def romanToInt(self, s: str) -> int:
        result = 0
        prev = 0
        for c in reversed(s):
            current = self.roman_map[c]
            if current >= prev:
                result += current
            else:
                result -= current
            prev = current
        return result


if __name__ == '__main__':
    s = "MCDLXXVI"
    print(Solution().romanToInt(s), 1476)
