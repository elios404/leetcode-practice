from collections import deque, Counter

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counter = Counter(senate)
        q = deque(senate)

        while counter["R"] > 0 and counter["D"] > 0:
            turn = q.popleft()
            if turn == ".":
                continue

            for i in range(len(q)):
                if turn != q[i] and q[i] != ".":
                    counter[q[i]] -= 1
                    q[i] = "."
                    break
            q.append(turn)
        
        if counter["D"] == 0:
            return "Radiant"
        else:
            return "Dire"
        