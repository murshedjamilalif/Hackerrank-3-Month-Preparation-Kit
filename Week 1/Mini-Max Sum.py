def miniMaxSum(numbers):
    minValue = numbers[0]
    totalSum = 0
    maxValue = numbers[0]
    for number in numbers:
        if number > maxValue:
            maxValue = number
        if number < minValue:
            minValue = number
        totalSum += number
    print(totalSum - maxValue, totalSum - minValue)

# Example usage:
miniMaxSum([1, 3, 5, 7, 9])
