class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[len(digits)-1] += 1 #add 1 

        for i in range(len(digits)-1, -1, -1):
            new = digits[i] + carry
            if new == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = new
        
        if carry == 1:
            digits = [1] + digits
        
        return digits