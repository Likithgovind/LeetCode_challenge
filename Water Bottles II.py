class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        e = 0       
        f = numBottles  
        d = 0     
        while f > 0:
            d += f 
            e += f 
            f = 0 
            if e >= numExchange:
                e -= numExchange  
                f += 1    
                numExchange += 1
        return d 
