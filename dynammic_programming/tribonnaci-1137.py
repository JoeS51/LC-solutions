class Solution:
    def tribonacci(self, n: int) -> int:
        arr = []
        arr.append(0)
        arr.append(1)
        arr.append(1)
        for i in range(3, n+1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        return arr[n]

# runtime: O(n)
# spacetime: O(n)
# notes: range() in python does not include n so we need to go to n+1
