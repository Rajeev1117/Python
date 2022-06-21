"""The selection sort algorithm sorts an array by repeatedly
finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning"""

def sort(nums):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)