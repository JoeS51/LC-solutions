class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1_map = defaultdict(int)
        n1_max = -1
        for i in nums1:
            n1_map[i] += 1
            n1_max = max(n1_max, i)

        n2_map = defaultdict(int)
        for j in nums2:
            n2_map[j] += 1

        ans = 0 
        for j in n2_map:
            divisor = k * j
            curr = 1
            product = curr * divisor
            while product <= n1_max:
                if product in n1_map:
                    ans += n1_map[product] * n2_map[j]
                curr += 1
                product = curr * divisor

        return ans

# runtime: O(n + m + for every unique j{m / k*j})
# spacetime: O(n)
