#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scoreList):
    maxScore = scoreList[0]
    minScore = scoreList[0]
    maxScoreCount = 0
    minScoreCount = 0
    
    for score in scoreList:
        if score > maxScore:
            maxScore = score
            maxScoreCount += 1
        if score < minScore:
            minScore = score
            minScoreCount += 1
    
    return [maxScoreCount, minScoreCount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
