class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        s = SortedSet()
        for i in range(len(mat[0])):
            s.add(mat[0][i])
        for i in range(len(mat)):
            curr_s = SortedSet()
            for j in range(len(mat[i])):
                curr_num = mat[i][j]
                if curr_num in s:
                    curr_s.add(curr_num)
            s = curr_s

        if (len(curr_s) == 0):
            return -1
        return curr_s[0]
