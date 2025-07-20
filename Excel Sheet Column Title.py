class Solution(object):
    def convertToTitle(self, columnNumber):
        res=""
        while columnNumber>0:
            columnNumber=columnNumber-1
            rem=columnNumber%26
            res=chr(65+rem)+res
            columnNumber=columnNumber//26
        return res
