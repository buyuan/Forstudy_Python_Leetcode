class Solution:
    def hIndex(self, citations: list[int]) -> int:
        #排序，然后从大到小依次查，什么时候当前这个值刚好不大于他的index，那么这个index就是答案
        #例如：
        # 0  1  2  3  4  5  6  7  8
        # 9  9  8  7  6  5  4  3  2
        #当index =5时候，前面5个文章，都大于五，后面的文章都不大于5
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]<=i:return i
        #n篇论文引用都大于n
        return len(citations)




'''
274. H-Index
Medium
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.
Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
'''