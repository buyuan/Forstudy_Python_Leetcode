class Solution:
    def maximumBooks(self, books: list[int]) -> int:
        #用dp，dp[i]表示，我必须拿第i个书架上的所有书，最终最多能拿多少本，换句话说实际也就是从0到i这段中间，所能拿到所有的最多的书
        #因为在i要拿books[i],means in i-1, at most books[i]-1
        #tkbooks[i-1]<=books[i]-1
        #tkbooks[i-2]<=books[i]-2   #1 book less than in i-1
        #.....
        #tkbooks[0]<=books[i]-i
        #sum(tkbooks[0]+)tkbooks[1]+....+tkbooks[i-1) <= i*books[i]-(1+2+3+...+i)
        #在i的左边的某个点，可能存在一个index j， 导致，books[j]<books[i]-(i-j),这样的话，在index j，无法取books[i]-(i-j)本书，那么
        #上面式子的等号无法成立，现在就是要找这样一个分界点,j的右边，延续上面的依次减一的规则，左边则是一路dp算上来的最大值
        #books[j]<books[i]-(i-j) =》 books[j]-j<books[i]-i, 定义nbooks[i] = books[i]-i
        #即：dp[i] = dp[j] + sum(tkbooks[j+1]+tkbooks[j+2]+...+tkbooks[i])
        #=>dp[i] = dp[j] + sum(tkbooks[j+1]+tkbooks[j+2]+...+tkbooks[i])
        # =dp[j]+sum(books[i]+books[i]-1+books[i]-2+...+books[i]-(i-j))
        # = dp[j]+(books[i]+books[i]-(i-j))*(i-j+1)//2
        #有可能某一个i，找不到对应的j（nbook数列往左没有更小的），则dp[j]就不能取，上面公式dp[j]和j都不能算进去


        n = len(books)
        nbooks = [books[i]-i for i in range(n)]
        index_smallerLeft = [-1]*n

        #先用单调递增栈求出index_smallerLeft,因为需要找到某个index左边第一个小的，所以从右往左扫描
        stk=[]
        for i in range(n-1,-1,-1):
            while stk and nbooks[stk[-1]]>nbooks[i]:
                index_smallerLeft[stk.pop()]=i
            stk.append(i)

        dp=[0]*n
        #只取第一个应该全取
        dp[0]=books[0]
        for i in range(1,n):
            j = index_smallerLeft[i]
            #下面注意找到差为1的等差数列的项数
             #i-j是指从i到j之间的实际项目数，看的是nbook这个数列，books[i],是指，严格等差1的数列，最多也只能取到books[i]项目，
             #不然就不够了，如果再往左继续-1，取得的个数就要小于0了，所以，如果books[i]够大，取实际项目数i-j.如果不够大，只取可以为正的哪部分books[i]
            count=min(i-j,books[i])
            #首项和末项,末项肯定就是book[i]，因为books[i]全取，首项是有可能按照公式等差为1，有多少项目，就减去多少个1
            first,last = books[i]-count+1,books[i]
            total = (first+last)*count//2 #这是j到i的一段等差为1的和
            #就是上面注释说的，如果没有符合条件的j，则算作0
            dp[i] = total + (0 if j==-1 else dp[j] )
        return max(dp)
        


       
        

       

'''
2355. Maximum Number of Books You Can Take
Hard
You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.

 

Example 1:

Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.
Example 2:

Input: books = [7,0,3,4,5]
Output: 12
Explanation:
- Take 3 books from shelf 2.
- Take 4 books from shelf 3.
- Take 5 books from shelf 4.
You have taken 12 books so return 12.
It can be proven that 12 is the maximum number of books you can take.
Example 3:

Input: books = [8,2,3,7,3,4,0,1,4,3]
Output: 13
Explanation:
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.
 

Constraints:

1 <= books.length <= 105
0 <= books[i] <= 105
'''