class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_words = [words[0]]
        actual_size = len(words[0])
        curr_size = len(words[0])
        output = []
        for i in range(1, len(words)):
            word = words[i]
            new_size = 0
            if len(curr_words) == 0:
                new_size = len(word)
            else:
                new_size = curr_size + len(word) + 1 # account for space between words
            if new_size <= maxWidth: # new word fits
                curr_size = new_size
                actual_size += len(word)
                curr_words.append(word)
                if i == len(words) - 1:
                    print("here")
                    curr_line = curr_words[0]
                    for j in range(1, len(curr_words)):
                        curr_line += " " + curr_words[j]
                    while len(curr_line) < maxWidth:
                        curr_line += " "
                    output.append(curr_line)
                    curr_words = []
            else: # doesn't fit
                curr_line = ""
                x = (maxWidth - actual_size)
                if len(curr_words) == 1:
                    num_spaces = x
                    curr_line += curr_words[0]
                    while num_spaces > 0:
                        curr_line += " "
                        num_spaces -= 1
                else:
                    num_spaces = x // (len(curr_words) - 1)
                    extra_spaces = x % (len(curr_words) - 1)
                    for j in range(0, len(curr_words)-1):
                        new_word = curr_words[j]
                        curr_line += new_word
                        if extra_spaces > 0:
                            curr_line += " "
                            extra_spaces -= 1
                        for space in range(num_spaces):
                            curr_line += " "
                    curr_line += curr_words[len(curr_words) - 1]
                output.append(curr_line)
                curr_words = [word]
                actual_size = len(word)
                curr_size = len(word)
        if len(curr_words) > 0:
            curr_line = curr_words[0]
            for j in range(1, len(curr_words)):
                curr_line += " " + curr_words[j]
            while len(curr_line) < maxWidth:
                curr_line += " "
            output.append(curr_line)
        return output
                
                    




