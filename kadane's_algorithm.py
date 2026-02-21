#Kadane’s Algorithm is an efficient algorithm used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
#Elements that are next to each other without any gap.

nums=[1,-2,-4,1,-5,3,-2,-1,9,-4,3]

max_sum=nums[0]
current_sum=nums[0]
for i in range(1,len(nums)):   
    current_sum=max(nums[i],current_sum+nums[i])
    max_sum=max(max_sum,current_sum)
print(max_sum)
