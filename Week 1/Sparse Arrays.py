def sparseArr(strings, queries):
    for query in queries:
        count = 0
        for string in strings:
            if query == string:
                count += 1
            else:
                continue
        print(count)

# Directly call the function
# numStrings = int(input())
# stringsList = []
# for _ in range(numStrings):
#     stringsList.append(input())
# numQueries = int(input())
# queriesList = []
# for _ in range(numQueries):
#     queriesList.append(input())
# sparseArr(stringsList, queriesList)

#Test Caes 1
strings = ['hello', 'world', 'hello', 'world']
queries = ['hello', 'world']
# Expected Output: 2 for 'hello' and 2 for 'world'
sparseArr(strings, queries)

#Test Caes 2
strings = ['hello', 'world', 'hello', 'world']
queries = ['python', 'java']
# Expected Output: 0 for 'python' and 0 for 'java'
sparseArr(strings, queries)

#Test Caes 3
strings = ['hello', 'world', 'hello', 'world']
queries = ['hello']
# Expected Output: 2 for 'hello'
sparseArr(strings, queries)

#Test Caes 4
strings = ['hello']
queries = ['hello', 'world']
# Expected Output: 1 for 'hello' and 0 for 'world'
sparseArr(strings, queries)

#Test Caes 5
strings = ['hello', 'world', 'hello', 'world']
queries = ['hello', 'hello']
# Expected Output: 2 for the first 'hello' and 2 for the second 'hello'
sparseArr(strings, queries)
