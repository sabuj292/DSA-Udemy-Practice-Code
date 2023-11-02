
# Write a program to find all pairs of integers whose sum is equal to a given number

# [2,6,3,9,11]    (9----------> [6,3])

# LeetCode 1-Two Sum

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]: # this loop need only when we need to omit same number
                continue
            elif nums[i] + nums[j] == target:
                print(nums[i], nums[j])


mylist =[1,2,3,2,3,4,5,6]
findPairs(mylist, 6)