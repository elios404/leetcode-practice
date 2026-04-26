class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def makeCombination(num: int, picked: list, k: int, n: int):
            if len(picked) == k and sum(picked) == n:
                ans.append(list(picked))
                return
            
            if num == 10 or len(picked) > k or sum(picked) > n:
                return
            
            picked.append(num)
            makeCombination(num+1, picked, k, n) # pick num
            picked.pop()
            makeCombination(num+1, picked, k, n) # pass num
        
        makeCombination(1, [], k, n)

        return ans