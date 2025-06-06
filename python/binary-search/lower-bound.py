        def binary_search(nums, lo, hi, val):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] >= val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo

