class Solution:
    def maxArea(self, height: list[int]) -> int:
        #从两头开始往中间走，这样循环次数减少
        ans = 0
        left, right = 0, len(height) - 1
        while (left < right):
            wd = right - left
            ht = 0
            if height[left] > height[right]:
                ht = height[right]
                right -= 1
            else:
                ht = height[left]
                left += 1
            ans = max(ans, ht * wd)
        return ans

'''
11. Container With Most Water
Medium
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''