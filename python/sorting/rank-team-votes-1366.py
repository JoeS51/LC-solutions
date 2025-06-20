class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = dict()

        for word in votes:
            for i, char in enumerate(word):
                if char not in d:
                    d[char] = [0] * len(word)
                d[char][i] += 1
        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key= lambda x: d[x], reverse=True))

# Time complexity: O(nlog(n)) because we are sorting at the end
# this lambda expression was weird it's basically a function like in java the -> syntax
