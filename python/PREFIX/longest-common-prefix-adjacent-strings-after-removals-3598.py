class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def find_longest(curr_words, offset):
            longest_pref = 0
            res = [0]
            if offset == 2:
                res = [0, 0]
            for j in range(offset, len(curr_words)):
                prev = curr_words[j-offset]
                curr = curr_words[j]
                curr_pref = 0
                for idx in range(len(curr)):
                    if idx < len(prev) and curr[idx] == prev[idx]:
                        curr_pref +=1
                    else:
                        break
                res.append(curr_pref)
            return res
        
        lcp = find_longest(words, 1)
        prev_word_lcp = find_longest(words, 2)
        print(lcp)
        left_max = []
        right_max = [0] * len(lcp)
        curr_max = 0
        for i in range(len(words)):
            curr_max = max(curr_max, lcp[i])
            left_max.append(curr_max)
        curr_max = 0
        for i in range(len(words)-1, -1, -1):
            curr_max = max(curr_max, lcp[i])
            right_max[i] = curr_max
        res = []

        for i in range(len(words)):
            prev_max = left_max[i-1] if i > 0 else 0
            after_max = right_max[i+2] if i +2 < len(words) else 0
            possible_max = 0
            if i > 0 and i + 1 < len(words):
                possible_max = prev_word_lcp[i+1]
            res.append(max(max(prev_max, after_max), possible_max))
        return res

# runtime: O(N)
# spacetime: O(N)
