# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        front, back = 1, n
        mid = (front + back) // 2

        # picked number is definitely betwenn 1~N
        while front <= back: # until mid == n
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1 :# mid is higher
                back = mid - 1
            elif res == 1:
                front = mid + 1

            mid = (front+back) // 2

        return -1