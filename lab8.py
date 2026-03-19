"""Design and implement C/JAVA/Python Program to find a subset of a given set S = 
{sl , s2,.....,sn} of n positive integers whose sum is equal to a given positive integer 
d. """


def subset_sum(nums, target):
    n = len(nums)
    
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    
    for i in range(n + 1):
        dp[i][0] = True

    
    for i in range(1, n + 1):
        current_val = nums[i-1]
        for j in range(1, target + 1):
            if j < current_val:
                
                dp[i][j] = dp[i-1][j]
            else:
                
                dp[i][j] = dp[i-1][j] or dp[i-1][j - current_val]


    found = dp[n][target]
    

    subset = []
    if found:
        curr_i, curr_j = n, target
        while curr_i > 0 and curr_j > 0:
            
            if dp[curr_i][curr_j] != dp[curr_i-1][curr_j]:
                subset.append(nums[curr_i-1])
                curr_j -= nums[curr_i-1]
            curr_i -= 1
            
    return found, subset


numbers = [3, 2, 7, 1]
goal = 6
is_possible, result_set = subset_sum(numbers, goal)

print(f"Is sum {goal} possible? {is_possible}")
if is_possible:
    print(f"Subset: {result_set}")
