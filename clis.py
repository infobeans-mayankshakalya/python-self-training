import sys
lst = sys.argv[1].split(',')
print(len(lst), lst)
j=1
for i in lst:
    j = int(i)*j
print(j)
print("Done")
print("Exiting the program")
sys.exit(0)
# This code takes a list of numbers from command line arguments, splits them by commas,
# calculates the product of those numbers, and prints the result.