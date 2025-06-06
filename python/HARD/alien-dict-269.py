class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        in_degree = {c: 0 for word in words for c in word} 
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            # prefixes are the same but length of first word is longer so invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        in_degree[w2[j]] += 1
                    adj[w1[j]].add(w2[j])
                    break

        output = []
        q = deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            c = q.popleft()
            output.append(c)
            for d in adj[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    q.append(d)
        
        if len(output) < len(in_degree):
            print("here")
            print(in_degree)
            print(output)
            return ""
        return "".join(output)

