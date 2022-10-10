class Solution:
    def isValid(self, s: str) -> bool:
        elements = list(s)
        stack = []
        for ele in elements:
            if(ele == '(' or ele == '[' or ele == '{'):
                stack.append(ele)
            else:
                if(len(stack) == 0):
                    return False
                temp = stack.pop()
                if(((ele == ')' and  temp!='(') or (ele == ']' and temp !='[') or (ele == '}' and temp !='{'))):
                    return False
        if(len(stack) != 0):
            return False
        else:
            return True
            