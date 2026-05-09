#n회 이상 인용된 논문의 수가 n개 일때 n의 최대값이 h-index 이다.
#n의 최대는 발표된 논문의 수 이다.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        cit_len = len(citations)
        h_index = 0
        for idx in range(cit_len):
            if idx == 0 or citations[idx] != citations[idx-1]:
                idxth_h_index = min(cit_len-idx, citations[idx])
                h_index = max(h_index, idxth_h_index)
        return h_index
