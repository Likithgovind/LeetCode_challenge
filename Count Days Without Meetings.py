class Solution(object):
    def countDays(self, days, meetings):
        meetings.sort()
        l=[]
        count=0
        for start,end in meetings:
            if l and start <= l[-1][1]:
                l[-1][1]=max(l[-1][1],end)
            else:
                l.append([start,end])
        meeting_days = sum(end - start + 1 for start, end in l)
        return days - meeting_days
days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
result = Solution()
print(result.countDays(days, meetings)) #output: 2
