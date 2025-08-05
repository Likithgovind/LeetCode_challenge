class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        for i in fruits:
            for j in baskets:
                if i<=j:
                    baskets.remove(j)
                    break
        return len(baskets) 
