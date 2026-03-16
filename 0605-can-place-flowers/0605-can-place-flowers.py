"""
1. Approach
    - search list sequentially and check whether that flower can be planted or not.
    - if i th flowerbed is 1 then i+1 th also can't use so move to i+2
    - if i th flowerbed is 0 then check i+1 th and if it's also 0 then plant a flower and move to i+2 th.
    - Additional! : if cnt is bigger than n, then of course numbers of N flowers can be planted , so return True
2. Time complexity : O(n), need to check the List once.
3. Space complexity : O(1), cnt which means how many flower can be planted only needed.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        i=0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == len(flowerbed)-1:
                    cnt+=1
                else:
                    if flowerbed[i+1] == 0:
                        cnt+=1
                        i+=1
                    else:
                        i+=2
            else:
                i+=1
            i+=1
        
        if cnt >= n:
            return True
        else:
            return False