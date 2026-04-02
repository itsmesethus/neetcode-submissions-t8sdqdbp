class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=f"{str(len(i))}#{i}"
        return s

    def decode(self, s: str) -> List[str]:
        result=[]
        left = 0
        while left < len(s):
            right=left
            while s[right]!='#':
                right+=1
            length= int(s[left:right])
            start_string=right+1
            end_string=length+start_string
            result.append(s[start_string:end_string])
            left = end_string
        return result
  
            
            
