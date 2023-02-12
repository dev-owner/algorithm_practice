from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # time: O(N+M)
        # space: O(N+M)
        morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        start_idx = ord('a')
        ret = set()
        for word in words:
            morse = []
            for c in word:
                idx = ord(c) - start_idx
                morse.append(morse_map[idx])
            ret.add(''.join(morse))

        return len(ret)

    def sol2(self, words):
        morse_map = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(morse_map[ord(i) - ord('a')] for i in w) for w in words})

if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    ans = Solution().sol2(words)
    print(f'{ans}, 2')
