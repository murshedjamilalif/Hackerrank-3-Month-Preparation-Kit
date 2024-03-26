# import os
# import sys

# def timeConversion(timeString):
#     timeParts = timeString.split(":")
#     if timeString[-2:] == "PM":
#         if timeParts[0] != "12":
#             timeParts[0] = str(int(timeParts[0]) + 12)
#     else:
#         if timeParts[0] == "12":
#             timeParts[0] = "00"
#     # Construct the new time string without using .join
#     newTime = timeParts[0] + ":" + timeParts[1] + ":" + timeParts[2][:2]
#     return newTime

# # Directly call the function
# f = open(os.environ['OUTPUT_PATH'], 'w')

# timeString = input()

# result = timeConversion(timeString)

# f.write(result + '\n')

# f.close()
import os
import sys

def timeConversion(timeString):
    timeParts = timeString.split(":")
    if timeString[-2:] == "PM":
        if timeParts[0] != "12":
            timeParts[0] = str(int(timeParts[0]) + 12)
    else:
        if timeParts[0] == "12":
            timeParts[0] = "00"
    newTime = ':'.join(timeParts)
    return str(newTime[:-2])

# Directly call the function
f = open(os.environ['OUTPUT_PATH'], 'w')

timeString = input()

result = timeConversion(timeString)

f.write(result + '\n')

f.close()
