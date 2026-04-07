"""
1. Approach:
    - This problem is union-find algorithm problem, I think.
    - We need to find distinguishable sets.
2. Time Complexity : O(N^2) - Nested for loops is primary time complexity.
3. Space Comeplextiy : O(N) - list for tracking root of every nodes.
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]

        # O(alpha(log N)) - At first, can be maximum log N(height of the tree) but after find, every node will be connected with root directly.
        def find(city_num: int) -> int:
            if root[city_num] == city_num:
                return city_num
            root[city_num] = find(root[city_num])
            return root[city_num]
        
        # O(1) ? - Not sure
        def union(num1: int, num2: int) -> bool:
            root1 = find(num1)
            root2 = find(num2)

            if root1 == root2:
                return False
            else:
                root[root2] = root1
                return True
        
        # O(n ^ 2) - sum of 1~n, n*(n+1)/2
        for i in range(n):
            for j in range(i+1,n): # why it can't be (i+1, n)? if j is i then isConnected[i][i] is always pointing itself, which has no meanig of union..?
                if isConnected[i][j] == 1:
                    union(i,j)
        
        ans = 0
        for i in range(n):
            if root[i] == i:
                ans += 1

        return ans