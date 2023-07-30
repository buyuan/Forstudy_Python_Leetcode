class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        #
        if date1<date2:
            date1,date2 = date2,date1
        y1,m1,d1 = [int(x) for x in date1.split("-")]
        y2,m2,d2 = [int(x) for x in date2.split("-")]

        #先计算两个年的日期差别，相当于从1月1日到另一个12月31日
        isLeap = lambda x: (x%4==0 and x%100!=0) or x%400==0

        day = 365*(y1-y2)
        for d in range(y2,y1):
            if isLeap(d):
                day+=1
        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        day+= days[m1-1]+(m1>2 and isLeap(y1))+d1
        day-= days[m2-1]+(m2>2 and isLeap(y2))+d2

        return day

'''
1360. Number of Days Between Two Dates
Easy
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.'''