
def max_independent_set(nums):
    
    #if all numbers are negatives
    if all( x<0 for x in nums):
        return []
    
    #create a cache and initialize its first value
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]

    #find max sum
    for i in range(2, len(nums)):
        dp[i] = max((dp[i-1] if dp[i-1] > 0 else 0), nums[i]+(dp[i-2] if dp[i-2] >0 else 0))

    #print nums used for max sum, referenced GeeksForGeeks
    result = []
    i = len(nums) -1 
    while i >= 0:
        if (i==0 or dp[i] != dp[i-1]) and nums[i] >=0:
            result.append(nums[i])
            i -=2 
        else:
            i-=1

    result = result[::-1]
    return result
