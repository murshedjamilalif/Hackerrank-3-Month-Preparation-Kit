def plusMinus(numbers):
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    
    for number in numbers:
        if number > 0:
            positiveCount += 1
        elif number == 0:
            zeroCount += 1
        else:
            negativeCount += 1
    
    print("{0:.6f}".format(positiveCount / len(numbers)))
    print("{0:.6f}".format(negativeCount / len(numbers)))
    print("{0:.6f}".format(zeroCount / len(numbers)))

# Directly call the function
# n = int(input())
# numbers = list(map(int, input().rstrip().split()))
# plusMinus(numbers)

#Test Case 1
numbers = [1, -1, 0, -2, 2]
# Expected Output: 0.400000, 0.400000, 0.200000
plusMinus(numbers)
    
#Test Case 2
numbers = [1, 2, 3, 4, 5]
# Expected Output: 1.000000, 0.000000, 0.000000
plusMinus(numbers)

#Test Case 3
numbers = [-1, -2, -3, -4, -5]
# Expected Output: 0.000000, 1.000000, 0.000000
plusMinus(numbers)

#Test Case 4
numbers = [0, 0, 0, 0, 0]
# Expected Output: 0.000000, 0.000000, 1.000000
plusMinus(numbers)

#Test Case 5
numbers = [1, -1, 2, -2, 3, -3]
# Expected Output: 0.500000, 0.500000, 0.000000
plusMinus(numbers)
