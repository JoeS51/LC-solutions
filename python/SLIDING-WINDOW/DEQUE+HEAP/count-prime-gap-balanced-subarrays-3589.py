class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        def sieve(n):
            isPrime = [True] * (n+1)
            isPrime[0] = isPrime[1] = False
            
            for (i, prime) in enumerate(isPrime):
                if prime:
                    for x in range(i*i, n+1, i):
                        isPrime[x] = False
        
            return isPrime

        isPrime = sieve(max(nums))
        primes_q = dequeue()
        minHeap = []
        maxHeap = []
        left = 0
        cnt = 0

        for i, val in enumerate(nums):
            # if not prime, then see if count goes up 
            if not isPrime[val]:
                if len(primes_q) >= 2:
                    # kinda complicated. basically you want to count all subarrays that are valid that go up until this index. 
                    # The valid subarrays are from the left most valid index to the left prime that fits the criteria
                    cnt += primes_q[-2] - left
                continue
            
            primes_q.append(i)
            heapq.heappush(minHeap, (val, i))
            heapq.heappush(maxHeap, (-val, i))

            while primes_q and (-maxHeap[0][0] - minHeap[0][0] > k):
                stalePrime = primes_q.popLeft()
                while minHeap and minHeap[0][1] <= stalePrime:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] <= stalePrime:
                    heapq.heappop(maxHeap)
                l = stalePrime


            if len(primes_q) >= 2 and (-maxHeap[0][0] - minHeap[0][0] > k):
                cnt += primes_q[-2] - left
        
        return cnt

