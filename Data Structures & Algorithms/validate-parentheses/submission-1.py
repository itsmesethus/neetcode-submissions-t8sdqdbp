class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dct={")":'(',
             "}":"{",
             "]":"["}

        for char in s:
            if char in "{([":   # openings
                stack.append(char)
            elif stack==[]: # not proper closing we got
                return False
            elif dct[char]!=stack[-1]:
                return False
            else:
                stack.pop()
        return stack==[]


            
        