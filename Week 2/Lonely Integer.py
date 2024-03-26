def checkElem(s):
    for i in range(0, len(s)):
        if s.count(s[i]) != 2:
            print(s[i])
        else:
            continue

# Directly call the function
n = int(input())
s = list(map(int, input().split()))
checkElem(s)