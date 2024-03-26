def divSumPairs(numElements, modulus, numbers):
    count = 0
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % modulus == 0:
                count += 1
            else:
                continue
    print(count)

# Directly call the function
# numElements, modulus = list(map(int, input().split()))
# numbers = list(map(int, input().split()))
# divSumPairs(numElements, modulus, numbers)

#Example 1
numElements, modulus = 4, 5
numbers = [1, 2, 3, 4]
divSumPairs(numElements, modulus, numbers)
    
#Example 2
numElements, modulus = 4, 5
numbers = [1, 2, 3, 4]
divSumPairs(numElements, modulus, numbers)

#Example 3
numElements, modulus = 4, 2
numbers = [2, 4, 6, 8]
divSumPairs(numElements, modulus, numbers)

#Example 4
numElements, modulus = 1, 1
numbers = [1]
divSumPairs(numElements, modulus, numbers)

#Example 5
numElements, modulus = 100, 10
numbers = [i for i in range(1, 101)]
divSumPairs(numElements, modulus, numbers)
