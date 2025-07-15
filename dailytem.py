class Solution:
    def dailyTemperatures(self, ts):
        result=[0]*len(ts)
        stack=[]
        for i in range(len(ts)):
            while stack and ts[i] > ts[stack[-1]]:
                index_value=stack.pop()
                result[index_value]=i-index_value
            stack.append(i)
        return result
