class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        positions = []
        vowels_to_sort = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                positions.append(i)
                vowels_to_sort.append(s[i])
        sorted_vowels = sorted(vowels_to_sort)
        print(sorted_vowels)
        res = ""
        j = 0
        for i in range(len(s)):
            if j < len(sorted_vowels) and i == positions[j]:
                res += sorted_vowels[j]
                j += 1
            else:
                res += s[i]
        return res
        
 

