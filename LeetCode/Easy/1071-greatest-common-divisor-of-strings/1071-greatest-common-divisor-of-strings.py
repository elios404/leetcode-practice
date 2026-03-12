"""
1. Approach
    - Use the property that if a common divisor string exists, str1 + str2 must equal str2 + str1.
    - If the condition holds, the length of the GCD string is the GCD of the two string lengths.
    - Utilize the math.gcd() function to find the optimal length and return the prefix.
2. Time Complexity : O(N + M), We check the string concatenation property once. 
3. Space Complexity : O(N + M), Creating the concatenated strings for verification. 
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]