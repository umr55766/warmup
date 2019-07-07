'''
Find the nearest smaller numbers on left side in an array
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.
Examples:

Input:  arr[] = {1, 6, 4, 10, 2, 5}
Output:         {_, 1, 1,  4, 1, 2}
First element ('1') has no element on left side. For 6, 
there is only one smaller element on left side '1'. 
For 10, there are three smaller elements on left side (1,
6 and 4), nearest among the three elements is 4.

Input: arr[] = {1, 3, 0, 2, 5}
Output:        {_, 1, _, 0, 2}
Expected time complexity is O(n).

https://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/
'''

array = [1, 6, 4, 10, 2, 5]
stack = []

for element in array:
    
    while (stack and stack[-1] > element):
        stack.pop()

    print(stack[-1] if stack else "_")

    stack.append(element)
