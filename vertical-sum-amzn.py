"""

Given a Binary Tree, find vertical sum of the nodes that are in same vertical line. Print all sums through different vertical lines.

Input:
First line of every test case consists of T test case. First line of every test case consists of N, denoting number of nodes. Second line of every test case consists of 3*N elements denoting , 2 integers and 1 character ,i.e., parent node , child node and character denotes which child.

Output:
Single line output, print the vertical sum from left to right.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
3
5 2 L 5 3 R 2 1 L
5
5 3 R 5 2 L 2 1 L 2 7 R 3 6 L
Output:
1 2 5 3 
1 2 18 3

URL : https://practice.geeksforgeeks.org/problems/vertical-sum/1

"""

def calculate_vertical_sum(sum, tree, node, distance):
    if distance in sum:
        sum[distance] += int(node)
    else:
        sum[distance] = int(node)
    if node in tree:
        if tree[node][0]:
            sum = calculate_vertical_sum(sum, tree, tree[node][0], distance-1)
        if tree[node][1]:
            sum = calculate_vertical_sum(sum, tree, tree[node][1], distance+1)
    return sum


s = "5 2 L 5 3 R 2 1 L"
s = s.split()
i = 0
tree = {}
childs = []

while i < len(s):
    temp = s[i: i+3]
    if temp[0] not in tree:
        tree[temp[0]] = [None, None]
    if temp[2] == "R":
        tree[temp[0]][1] = temp[1]
    else:
        tree[temp[0]][0] = temp[1]
    i += 3
    childs.append(temp[1])

root = [temp for temp in tree if temp not in childs][0]

sums = calculate_vertical_sum({}, tree, root, 0)

print(" ".join([str(sums[distance]) for distance in sorted(sums)]))
