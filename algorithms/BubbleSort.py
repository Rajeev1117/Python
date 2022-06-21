"""Bubble sort is a sorting algorithm that compares two adjacent
elements and swaps them until they are not in the intended order."""

def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)