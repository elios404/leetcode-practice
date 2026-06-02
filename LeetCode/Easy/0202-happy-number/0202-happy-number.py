class Solution:
    def isHappy(self, n: int) -> bool:
        calculated_already = set()

        def process(number: int, s: set) -> bool:
            each_num = []
            while number != 0:
                each_num.append(number%10)
                number = number//10
            
            processed_number = 0
            for num in each_num:
                processed_number += num**2
            if processed_number == 1:
                return True
            
            if processed_number in s:
                return False
            else:
                s.add(processed_number)
                return process(processed_number, s)
        
        return process(n, calculated_already)
        