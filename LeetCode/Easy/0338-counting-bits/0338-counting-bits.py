class Solution:
    def countBits(self, n: int) -> List[int]:
        # 그 전의 2^N(?) 정도를 확인하면, 거기에 1을 더한 것이 현재의 1의 갯수이다. 약간 DP 처럼 풀면 될 듯?
        if n==0:
            return [0]
        elif n==1:
            return [0,1]
        
        ret = [0,1]
        cnt = 2 #2 부터 시작
        cnt_double = cnt * 2 # 4가 오기 전까지
        for i in range(2,n+1):
            if i == cnt_double: # 다음 2의 지수 수가 왔을 때
                ret.append(1)
                cnt = cnt_double
                cnt_double = cnt * 2
            else:
                ret.append(ret[i-cnt] + 1) # 자기 아래 수를 처음부터 갯수를 가져오기

        return ret