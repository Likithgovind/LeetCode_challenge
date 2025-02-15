lass Solution(object):
    def punishmentNumber(self, n):
        l = [1, 9, 10, 36, 45, 55,82, 91, 99, 100, 235, 297,369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        x=0
        for i in l:
            if n>=i:
                x=x+(i**2)
            else:
                break
        return x
n=10
ans=Solution()
result=ans.punishmentNumber(n)
print(result)
