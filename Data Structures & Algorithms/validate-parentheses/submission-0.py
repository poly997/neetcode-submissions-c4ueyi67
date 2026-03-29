class Solution:
    def isValid(self, s: str) -> bool:

        status = True
        stack = []
        index = 0

        for par in s:
            if par == "(" or par == "{" or par == "[":
                stack.append(par)
            elif par ==  "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    status = False
            elif par ==  "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    status = False
            elif par ==  ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    status = False
        if stack:
            status = False
        
        return status
            

        


            
        