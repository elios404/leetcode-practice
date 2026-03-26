"""
1. Time Complexity : O(N^2)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = []
        # O(N)
        for num in asteroids:
            l.append(num)
            while len(l) >= 2:
                right = l.pop()
                left = l.pop()

                # 0. if left and right are in same direction or if left is - and right is +
                if (left>0 and right>0) or (left < 0 and right < 0) or (left < 0 and right > 0):
                    l.append(left)
                    l.append(right)
                    break                    

                # 1. if left and right are same value, differnt direction
                if abs(left) ==  abs(right):
                    break

                # 2. if left > right
                if abs(left) > abs(right):
                    l.append(left)
                    break
                
                # 4. if left < right : continue
                if abs(left) < abs(right):
                    l.append(right)
         
        return l



        