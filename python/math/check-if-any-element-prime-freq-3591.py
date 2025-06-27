class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def sieve(n):
            isPrime = [True] * (n+1)
            if n == 1 or n == 0:
                return [False, False]
            isPrime[0] = isPrime[1] = False
            for i in range(2, n+1):
                j = i * i
                while j <= n:
                    isPrime[j] = False
                    j *= i
            return isPrime
        counts = Counter(nums)
        max_num = 0
        for i in counts:
            max_num = max(max_num, counts[i])
        isPrime = sieve(max_num)
        for i in counts:
            if isPrime[counts[i]]:
                return True
        return False
# runtime: O(n)
# spacetime: O(n)