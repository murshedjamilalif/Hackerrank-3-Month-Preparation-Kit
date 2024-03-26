
def splitString(inputString):
    if inputString[2] == "M":
        modifiedString = ""
        for i in range(4, len(inputString) - 2):
            if inputString[i] >= 'A' and inputString[i] <= 'Z':
                modifiedString = modifiedString + " " + chr(ord(inputString[i]) + 32)
                continue
            modifiedString += inputString[i]
        print(modifiedString.rstrip())
    elif inputString[2] == "C":
        modifiedString = chr(ord(inputString[4]) + 32)
        for i in range(5, len(inputString)):
            if inputString[i] >= 'A' and inputString[i] <= 'Z':
                modifiedString = modifiedString + " " + chr(ord(inputString[i]) + 32)
                continue
            modifiedString += inputString[i]
        print(modifiedString.rstrip())
    else:
        modifiedString = ""
        for i in range(4, len(inputString)):
            if inputString[i] >= 'A' and inputString[i] <= 'Z':
                modifiedString = modifiedString + " " + chr(ord(inputString[i]) + 32)
                continue
            modifiedString += inputString[i]
        print(modifiedString.rstrip())

def combString(combinedString):
    combinedStringResult = ""
    if combinedString[2] == "V":
        for i in range(4, len(combinedString), 1):
            if combinedString[i] == " ":
                combinedStringResult += ""
                continue
            if combinedString[i - 1] == " ":
                combinedStringResult += chr(ord(combinedString[i]) - 32)
                continue
            combinedStringResult += combinedString[i]
        print(combinedStringResult.rstrip())
    elif combinedString[2] == "C":
        combinedStringResult = chr(ord(combinedString[4]) - 32)
        for i in range(5, len(combinedString)):
            if combinedString[i] == " ":
                combinedStringResult += ""
                continue
            if combinedString[i - 1] == " ":
                combinedStringResult += chr(ord(combinedString[i]) - 32)
                continue
            combinedStringResult += combinedString[i]
        print(combinedStringResult.rstrip())
    else:
        for i in range(4, len(combinedString), 1):
            if combinedString[i] == " ":
                combinedStringResult += ""
                continue
            if combinedString[i - 1] == " ":
                combinedStringResult += chr(ord(combinedString[i]) - 32)
                continue
            combinedStringResult += combinedString[i]
        print(combinedStringResult + "()".rstrip())

# Directly call the functions
# while True:
#     try:
#         st = input().rstrip()
#         if st[0] == "S":
#             splitString(st)
#         elif st[0] == "C":
#             combString(st)
#         else:
#             break
#     except (EOFError):
#         break
#Test Case 1
inputString = "S MHelloWorld"
# Expected Output: "hello world"
splitString(inputString)
    
#Test Case 2
combinedString = "C Vhello world"
# Expected Output: "Hello World"
combString(combinedString)

#Test Case 3
inputString = "S CHelloWorld"
# Expected Output: "Hello World"
splitString(inputString)

#Test Case 4
combinedString = "C CHelloWorld"
# Expected Output: "Hello World"
combString(combinedString)

#Test Case 5
inputString = "S MHello!World"
# Expected Output: "hello! world"
splitString(inputString)
