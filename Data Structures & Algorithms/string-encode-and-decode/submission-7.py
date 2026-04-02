class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+= f'{len(i)}#{i}'
        return s

    def decode(self, s: str) -> List[str]:

        # output: 5#Hello5#World
        left=0
        res=[]
        while left < len(s):
            right=left
            while s[right]!='#':
                right+=1
            s_length=int(s[left:right])
            start_str=right+1 # 2
            end_str=s_length+start_str # 7
            res.append(s[start_str:end_str])
            left=end_str
        return res
            
            


