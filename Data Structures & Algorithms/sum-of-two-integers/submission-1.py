class Solution:
    def getSum(self, a: int, b: int) -> int:
        #return int(math.log(math.exp(a) * math.exp(b)))

        mask = 0xFFFFFFFF  # To keep it within 32 bits
        
        while b & mask: # While there is still a carry
            # 1. Find the carry bits and shift them left
            carry = (a & b) << 1
            # 2. XOR gives the sum without the carry
            a = a ^ b
            # 3. Update b to be the carry for the next round
            b = carry
            
        # Handle Python's infinite integer precision for negative results
        return (a & mask) if b > mask else a
      
        