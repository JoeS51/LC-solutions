class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        res = []
        def backtrack(curr_word, curr_sentence, syn_map, word_map, text):
            nonlocal res
            if curr_word >= len(text):
                res.append(curr_sentence.strip())
                return curr_sentence
            word = text[curr_word]
            if word not in word_map:
                curr_sentence += " " + word
                return backtrack(curr_word+1, curr_sentence, syn_map, word_map, text)
            for possible_word in syn_map[word_map[word]]:
                backtrack(curr_word + 1, curr_sentence + " " + possible_word, syn_map, word_map, text)
            return 


        word_map = {}
        syn_map = {}
        adj_list = {}
        curr = 0
        for i in synonyms:
            word1 = i[0]
            word2 = i[1]
            if word1 not in word_map and word2 not in word_map:
                word_map[word1] = curr
                word_map[word2] = curr
                syn_map[curr] = [word1, word2]
                curr += 1
            elif word1 not in word_map:
                ind = word_map[word2]
                word_map[word1] = ind
                syn_map[ind].append(word1)
            elif word2 not in word_map:
                ind = word_map[word1]
                word_map[word2] = ind
                syn_map[ind].append(word2)
            else:
                # take lesser index
                j = word_map[word1]
                k = word_map[word2]
                print(j)
                print(k)
                print(word1)
                print(word2)
                
                if j < k:
                    temp = syn_map[k]
                    for z in temp:
                        word_map[z]= j
                    syn_map[j].extend(temp)
                    del syn_map[k]
                    word_map[word1] = j
                    word_map[word2] = j
                else:
                    temp = syn_map[j]
                    for z in temp:
                        word_map[z]= k
                    syn_map[k].extend(temp)
                    del syn_map[j]
                    word_map[word1] = k
                    word_map[word2] = k
        for i in syn_map:
            syn_map[i].sort()
        print(syn_map)
        print(word_map)
        
        backtrack(0, "", syn_map, word_map, text.split())

        return res

        

