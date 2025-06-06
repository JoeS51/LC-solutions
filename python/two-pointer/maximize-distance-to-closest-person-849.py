# for every 1 check who the closest person is to you. by iterating out left and right
# for the first person you see that is the closest
# if you reach an edge on either side then keep iterating on the other side


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist_to_person = 0
        dist_map_left = {}
        left_seat = -1
        for i, val in enumerate(seats):
            if val == 1:
                left_seat = i
            else:
                dist_map_left[i] = left_seat
        right_seat = len(seats)
        for i, val in enumerate(reversed(seats)):
            actual_i = len(seats) - i - 1
            if val == 1:
                right_seat = actual_i 
            else:
                if dist_map_left[actual_i] == -1:
                    left_dist =100000000
                else:
                    left_dist = actual_i - dist_map_left[actual_i]
                if right_seat == len(seats):
                    right_dist = 1000000000
                else:
                    right_dist = right_seat - actual_i
                print(left_dist)
                print(right_dist)
                print()
                curr_dist = min(left_dist, right_dist)
                max_dist_to_person = max(curr_dist, max_dist_to_person)
        return max_dist_to_person


        # for i, val in enumerate(seats):
        #     if val == 0:
        #         left_seat = i - 1
        #         right_seat = i + 1
        #         while (left_seat >= 0 and seats[left_seat] == 0):
        #             left_seat -= 1

        #         while (right_seat < len(seats) and seats[right_seat] == 0):
        #             right_seat += 1

        #         curr_max_dist = min(i - left_seat, right_seat - i)
        #         if left_seat < 0:
        #             curr_max_dist = right_seat - i
        #         elif right_seat == len(seats):
        #             curr_max_dist = i - left_seat
        #         max_dist_to_person = max(max_dist_to_person, curr_max_dist)
        # return max_dist_to_person

                    

