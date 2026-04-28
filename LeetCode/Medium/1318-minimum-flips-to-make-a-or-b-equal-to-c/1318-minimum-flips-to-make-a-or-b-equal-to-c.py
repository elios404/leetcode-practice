class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        
        while a > 0 or b > 0 or c > 0:
            # Bitwise AND to extract the Right-most bit (LSB)
            a_bit, b_bit, c_bit = a & 1, b & 1, c & 1
            
            if (a_bit | b_bit) != c_bit:
                # Your brilliant logic remains exactly the same!
                if a_bit == 1 and b_bit == 1:
                    ret += 2
                else:
                    ret += 1
            
            # Bitwise Right Shift to divide by 2 and push the next bit to the end
            a >>= 1
            b >>= 1
            c >>= 1
            
        return ret