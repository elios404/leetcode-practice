class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        code = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }

        l = len(digits)
        ans = []
        def makePossiblePasswords(idx:int, password_list:list, l:int):
            if idx == l:
                password = "".join(password_list)
                nonlocal ans
                ans.append(password)
                return

            digit = digits[idx]
            letters = code[digit]
            for letter in letters:
                password_list.append(letter) # put
                makePossiblePasswords(idx+1, password_list, l)
                password_list.pop() # remove
        
        makePossiblePasswords(0,[],l)

        return ans