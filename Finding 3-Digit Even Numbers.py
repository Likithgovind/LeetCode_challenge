class Solution(object):
    def findEvenNumbers(self, digits):
        result=[]
        n = len(digits)
        seen = set()
        for i in range(n):
            if digits[i] == 0:
                continue 
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0: 
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if num not in seen:
                            seen.add(num)
                            result.append(num)
        result.sort()
        return result
