class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        binary_a = [False] * (max_len)
        binary_b = [False] * (max_len)

        for i in range(len(a)-1, -1, -1):
            binary_a[len(a)-1-i] = True if a[i] == "1" else False
        for i in range(len(b)-1, -1, -1):
            binary_b[len(b)-1-i] = True if b[i] == "1" else False

        ret = []
        upper = False
        for i in range(max_len):
            # print(binary_a[i], binary_b[i], upper)
            calc = binary_a[i] + binary_b[i] + upper
            ret.append("1" if calc % 2 == 1 else "0") 
            upper = True if calc >= 2 else False
        
        if upper:
            ret.append("1")
        answer = "".join(ret[::-1])
        print(answer)
        return answer
