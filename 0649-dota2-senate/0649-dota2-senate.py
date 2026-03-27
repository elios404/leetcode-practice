from collections import deque, Counter

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counter = Counter(senate)
        q = deque(senate)

        cnt = 0
        while counter["R"] > 0 and counter["D"] > 0:
            turn = q.popleft()
            cnt += 1
            while cnt > 0:
                if turn != q[0]:
                    banned = q.popleft()
                    counter[banned] -= 1
                    if counter[banned] == 0:
                        break
                    cnt -= 1
                else:
                    q.append(turn)
                    q.popleft()
                    cnt += 1
            
            q.append(turn)
        
        if counter["D"] == 0:
            return "Radiant"
        else:
            return "Dire"
        