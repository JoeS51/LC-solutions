class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = defaultdict(int)
        res = 0
        max_same = 0
        max_l = ''
        for w in words:
            freq[w] += 1
            if w[0] == w[1]:
                if freq[w] > max_same:
                    max_l = w
                    max_same = freq[w]

        # freq[max_l] = 0
        # res += max_same * 2
        not_used = True
        for f in freq:
            if f == '':
                continue
            a, b = f[0], f[1]
            compliment = str(b + a)
            if a == b:
                if not_used and freq[f] % 2 != 0:
                    not_used = False
                    res += 2
                res += (freq[f] // 2) * 4
                continue
            if compliment in freq:
                res += min(freq[f], freq[compliment]) * 4
                freq[f] = 0
        return res


# BETTER SOLUTION:

def longestPalindrome(self, words: List[str]) -> int:
    m = defaultdict(int)
    unpaired = ans = 0
    for w in words:
        if w[0] == w[1]:
            if m[w] > 0:
                unpaired -= 1
                m[w] -= 1
                ans += 4
            else: 
                m[w] += 1
                unpaired += 1
        else:
            if m[w[::-1]] > 0:  # w[::-1] -> reversed w
                ans += 4
                m[w[::-1]] -= 1
            else: m[w] += 1
    if unpaired > 0: ans += 2
    return ans
