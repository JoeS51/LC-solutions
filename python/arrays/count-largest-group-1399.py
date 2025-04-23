class Solution:
    def countLargestGroup(self, n: int) -> int: 
        def sum_digits(n: int) -> int:
            sum = 0
            for i in str(n):
                sum += int(i)
            return sum
        groups = {}
        max_size = 0
        for i in range(1, n+1):
            curr_sum_of_digits = sum_digits(i)
            if curr_sum_of_digits not in groups:
                groups[curr_sum_of_digits] = 0
            # groups[curr_sum_of_digits] = 0 if curr_sum_of_digits not in groups
            groups[curr_sum_of_digits] += 1
            max_size = max(max_size, groups[curr_sum_of_digits])
        count = 0
        print("max" + str(max_size))
        for i in groups:
            print(groups[i])
            print(i)
            print()
            if groups[i] == max_size:
                count += 1
        return count

