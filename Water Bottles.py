class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        s = numBottles
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            s += new_bottles
            numBottles = numBottles // numExchange + numBottles % numExchange
        return s
