class Solution:
    def isHappy(self, n: int) -> bool:
        calced = set()

        def process(number: int, s: set) -> bool:
            next_number = 0
            while number != 0:
                next_number += (number%10)**2
                number = number//10
            
            if next_number == 1:
                return True

            if next_number in s:
                return False
            else:
                s.add(next_number)
                return process(next_number, s)
        
        return process(n, calced)
        