class Solution:
    def simplifyPath(self, path: str) -> str:
        keywords = path.split("/")
        
        address = []
        for keyword in keywords:
            if keyword == '':
                continue
            elif keyword == '.':
                continue
            elif keyword == '..':
                if address:
                    address.pop()
            else:
                address.append(keyword)
        
        path = ""
        for addr in address:
            path = path + "/" + addr
        
        return path if path != "" else "/"

        