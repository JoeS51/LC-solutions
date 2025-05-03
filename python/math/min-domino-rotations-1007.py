"""
can only be max between two diff numbers
see which numbers are on every line
"""




class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        possible_1 = tops[0] 
        possible_2 = bottoms[0]
        top_count_1 = int()
        top_count_2 = int()
        bottom_count_1 = int()
        bottom_count_2 = int()
        for i in range(len(tops)):
            top_num = tops[i]
            bottom_num = bottoms[i]
            if top_num == possible_1:
                top_count_1 += 1
            elif top_num == possible_2:
                top_count_2 += 1
            
            if bottom_num == possible_1:
                bottom_count_1 += 1 
            elif bottom_num == possible_2:
                bottom_count_2 += 1

            if possible_1 != top_num and possible_1 != bottom_num:
                possible_1 = -1
            if possible_2 != top_num and possible_2 != bottom_num:
                possible_2 = -1
            if possible_1 == -1 and possible_2 == -1:
                return -1
        n = len(tops)
        if possible_1 == -1:
            return min(n - top_count_2, n - bottom_count_2)
        elif possible_2 == -1:
            return min(n - bottom_count_1, n - top_count_1)
        else:
            min_1 = min(n - bottom_count_1, n - top_count_1)
            min_2 = min(n - top_count_2, n - bottom_count_2)
            return min(min_1, min_2)
        return 1
        
# really bad solution because it's hard to understand
# better solution using a method
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def countDifference(A, B, num):
            countA, countB = 0, 0
            
            for i in range(len(A)):
                # if we have a domino which doesn't have num at all, num can't be the whole row:
                if A[i] != num and B[i] != num:
                    return -1
                else:
                    if A[i] != num: countA+=1
                    if B[i] != num: countB+=1
    
            return min(countA, countB)
        
        # check if A[0] and B[0] can't be the number for the whole row:
        if A.count(A[0]) + B.count(A[0]) < len(A) and A.count(B[0]) + B.count(B[0]) < len(A):
            return -1
        
        # first try to make A[0] the whole row, then try B[0]:
        res1 = countDifference(A, B, A[0])
        res2 = countDifference(A, B, B[0])
        
        if min(res1, res2) > 0: return min(res1, res2)
        return max(res1, res2)


