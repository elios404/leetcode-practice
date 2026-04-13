class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ret = []

        potion_length = len(potions)
        for spell in spells:
            left, right = 0, potion_length

            while left < right:
                mid = (left + right) // 2
                # print(left, mid, right)
                product = spell * potions[mid]

                if product < success: #if product is smaller, then potion should be bigger
                    left = mid+1
                
                else:
                    right = mid
                
            cnt = potion_length - left
            ret.append(cnt)

        return ret