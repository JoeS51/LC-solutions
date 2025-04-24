class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = set(nums)
        curr_count = defaultdict(int)
        r = 0
        count = 0
        for l in range(len(nums)):
            if l > 0:
                prev_num = nums[l-1]
                curr_count[prev_num] -= 1
                if curr_count[prev_num] == 0:
                    curr_count.pop(prev_num)
            while r < len(nums) and len(curr_count) != len(unique):
                curr_count[nums[r]] += 1
                r += 1
            if len(curr_count) == len(unique):
                print(r)
                print(l)
                count += len(nums) - r + 1
        return count

        # unique = set()
        # for i in nums:
        #     unique.add(i)
        # curr_set = set()

        # count = 0
        # for i in range(len(nums)):
        #     curr_set = set()
        #     for j in range(i, len(nums)):
        #         curr_set.add(nums[j])
        #         if curr_set == unique:
        #             count += 1
        # return count


# runtime: O(n)
# complexity: O(n)
