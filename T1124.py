class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        #大于8看成1，小于看成-1，这道题简化成最长的连续数组，其值大于0，实际就是等于1，因为如果是2，至少还可以往前走或者前面往前再走一步，所以
        #连续数组的和等于1是解
        #用hash表，记录第一次出现的累加值的坐标，如-1，0，1的位置，往后累加，当发现，1。当累加到一个点i，累加值为1时，则从头到此，就是答案，因为从0开始到这里，
        #为1，符合条件，2。如果累加到i的值为0，那么从第一个累加为1的点开始，到这里，就是最大值。
        #以此类推，当到达i点时，如果累加为sum，则需要找一个index，第一次出现一个值，累加到index，合计为sum-1，这样，才能保证
        #index到i，中间的和等于1 （sum-（sum-1））=1，
        #换一种说法， sum((0~B))-sum((0~A))实际就是sum（B～A）

        dic = {}
        ans = 0
        sum = 0
        for i in range(len(hours)):
            sum += 1 if hours[i]>8 else -1
            if sum>0:
                #说明从头到此处就是答案，最长的数组长度，都不需要用max比较
                ans=i+1
            else:
                if not dic.__contains__(sum):
                    #如果这个累加值第一次出现，存下来
                    dic[sum]=i
                if dic.__contains__(sum-1):
                    #如果存在一个坐标index，使得累加到index 值为sum-1
                    ans = max(ans,i-dic[sum-1])
        return ans


'''
1124. Longest Well-Performing Interval
Medium
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.



Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0


Constraints:

1 <= hours.length <= 104
0 <= hours[i] <= 16'''