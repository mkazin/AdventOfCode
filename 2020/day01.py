# Solution to Advent of Code 2020, day 1
# https://adventofcode.com/2020/day/1
from util import load_data

EXAMPLE_INPUT = """1721
979
366
299
675
1456"""
EXPECTED_EXAMPLE_A = 514579
EXPECTED_EXAMPLE_B = 241861950

TARGET = 2020

def findProductOfTarget(input, target):

    # print("Searching for two items which sum to ", target, " in ", input)
    # Establish head and tail index pointers to begining and end of list
    head = 0
    tail = len(input) - 1

    # Loop until we find an answer (returns) or the pointers meet (i.e. no answer found)
    while head <= tail:
        # Check the current items at head and tail to see if they sum to our target
        sum = input[head] + input[tail]
        if sum == target:
            print(f"Found members: {input[head]}, {input[tail]}", end = '')
            # Return their product
            return input[head] * input[tail]
        elif sum < target:
            # If the sum is less than the target, we increase
            # the next sum by advancing the head pointer
            head += 1
        else:
            # And if the sum is above the target, we want to decrease
            # the next sum by decrementing the tail pointer
            tail -= 1

    return None

# Convert text data to a list of integers
example_input = list(map(lambda x: int(x.strip()), EXAMPLE_INPUT.split('\n')))

# Now sort that list (will be in ascending order). This allows 
# us to make a single pass over the list (O(n)) rather than use a nested loop (O(n^2))
example_input.sort()

print("Example dataset, expecting 1721 * 299 = 514579")
answer = findProductOfTarget(example_input, TARGET)
print(f"\nAnswer: {answer}")
assert(answer == EXPECTED_EXAMPLE_A)

print('\n\nRunning my input data:')
INPUT = load_data('Data/day01.txt')
# Convert text data to a list of integers
input = list(map(lambda x: int(x.strip()), INPUT))

# Now sort that list (will be in ascending order). This allows 
# us to make a single pass over the list (O(n)) rather than use a nested loop (O(n^2))
input.sort()

print(f"\nAnswer to submit: {findProductOfTarget(input, TARGET)}")

print("\n***** Part Two *****\n")

print("Example dataset, expecting 979 * 366 * 675 = 241861950")
answer = None
for leftIndex in range(len(example_input)-2):
    result = findProductOfTarget(example_input[leftIndex:], TARGET - example_input[leftIndex])
    if result:
        print(f", {example_input[leftIndex]}")
        answer = result * example_input[leftIndex]
        print(f"Answer: {answer}")
        break
assert(answer == EXPECTED_EXAMPLE_B)

print('\n\nRunning my input data:')

for leftIndex in range(len(input)-2):
    result = findProductOfTarget(input[leftIndex:], TARGET - input[leftIndex])
    if result:
        print(f", {input[leftIndex]}")
        print(f"Answer to submit: {result * input[leftIndex]}")
        break

