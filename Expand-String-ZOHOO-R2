"""
INPUT : a(b(c){2}){2}d
OUTPUT : abccbccd

INPUT : ((x){3}(y){2}z){2}
OUTPUT : xxxyyzxxxyyz
"""

string = "a(b(c){2}){2}d"
stack = []
i = 0
while i < len(string):
    if string[i] == "{":
        stack.append(stack.pop()*int(string[i+1]))
        i += 2
    elif string[i] == ")":
        peek = stack.pop()
        temp = ""
        while peek != "(":
            temp = peek + temp
            peek = stack.pop()
        stack.append(temp)
    else:
        stack.append(string[i])
    i += 1

print("".join(stack))
