"""Insertion sort involves finding the right place for a given element in a sorted list.
So in beginning we compare the first two elements and sort them by comparing them.
Then we pick the third element and find its proper position among the previous two sorted elements."""


def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)