'''
Problem Description
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.
Problem Constraints
1 <= A <= 10^3
1 <= B <= 10^9
1 <= C[i] <= 10^6
Input Format
The first argument is the integer A.
The second argument is the integer B.
The third argument is the integer array C.
Output Format
Return a single integer which denotes the maximum sum.
Example Input
Input 1:	A = 5	B = 12	C = [2, 1, 3, 4, 5]
Input 2:	A = 3	B = 1	C = [2, 2, 2]
Example Output
Output 1:	12
Output 2:	0
Example Explanation
Explanation 1:	We can select {3,4,5} which sums up to 12 which is the maximum possible sum.
Explanation 2:	All elements are greater than B, which means we cannot select any subarray.
Hence, the answer is 0.
'''



def maximum_subarr_sum(A,B,C):
    max_sum = 0
    curr_sum = 0
    start = 0
    for i in range(A):
        curr_sum += C[i]
        while curr_sum > B:
            curr_sum -= C[start]
            start += 1
        max_sum = max(max_sum, curr_sum)
    return max_sum
A1 = 5
B1 = 12
C1 = [2, 1, 3, 4, 5]

print(maximum_subarr_sum(A1,B1,C1))#12
A = 3	
B = 1	
C = [2, 2, 2]
print(maximum_subarr_sum(A,B,C))#0
