# Sample Input
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        for i in range(m+n-1, -1, -1):
            if pointer1 < 0 or pointer2 < 0:
                break
            val1 = nums1[pointer1]
            val2 = nums2[pointer2]
            if val1 > val2:
                nums1[i] = val1
                pointer1 -= 1
            else:
                print(i)
                nums1[i] = val2
                pointer2 -= 1

        while pointer2 >= 0:
            num1[pointer2] = nums2[pointer2]
            pointer2 -= 1
        
        return nums1

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]

    print(sol.merge(nums1, 3, nums2, len(nums2)))
