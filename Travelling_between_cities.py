'''
You are given positions of cities situated on X axis. The position of the city is denoted by array value .You have a bike which can travel exactly unit distance once the tank is full and each city has a fuel pump. Now you have to answer

queries where each query is of the following form.

:- Find the number of cities lying in the index range that you can reach from the city at index

    .

Constraints:

Note :- Use fast i/o.

Format of the input file:
First line :
i.e Number of testcases.
For each testcase :
First line : Three space separated integers  , and .
Second line : space separated integers denoting the location of cities .
Next lines : Three space separated

integers denoting the query.

Format of the output file:
Output the answer to each query in a separate line.
Sample Input

1

5 2 2

4 3 1 9 6

1 3 5 

1 5 2

Sample Output

3 

4

Explanation

For second query you can reach all the cities from city with location 3(index 2) except the city with location 9(index 4) that lie in the range [1,5] of the array location[i]. Note that X , L and R are indexes of the array.
Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
Time Limit: 2.0 sec(s) for each input file
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes
Allowed Languages: Go, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Lua, Python, Python 3, Scala
'''

# Write your code here

def process_test_case():
    n, k, q = [int(_) for _ in input().split()]
    original_data = [int(_) for _ in input().split()]
    data = sorted(original_data)
    query = []
    base = data[0]
    indexes = {}
    visitable_groups = [[]]
    c = 0
    for current_city in data:
        if abs(current_city - base) <= k:
            visitable_groups[c].append(current_city)
        else:
            c += 1
            visitable_groups.append([current_city])
        base = current_city
        indexes[current_city] = c
    # print(indexes)
    while q > 0:
        l, r, x = [int(_)-1 for _ in input().split()]
        visited_cities = []
        base = original_data[x]
        print(len(set(visitable_groups[indexes[base]]).intersection(original_data[l:r+1])))
                
        q -= 1
    
test_case = int(input())
while test_case > 0:
    process_test_case()
    test_case -= 1
