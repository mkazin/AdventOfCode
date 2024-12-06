"""

...

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

...

75,47,61,53,29
97,61,53,29,13
75,29,13
These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.

Of course, you'll need to be careful: the actual list of page ordering rules is bigger and more complicated than the above example.

Determine which updates are already in the correct order. What do you get if you add up the middle page number from those correctly-ordered updates?


"""

import functools


DEBUG = False

statement_datafile = 'Data/day05-statement.txt'
solve_datafile = 'Data/day05.txt'
rules = []
updates = []

def load_data(filename):
    rules.clear()
    updates.clear()
    with open(filename, 'r') as fp:
	    lines = fp.readlines()

    line = 0

    while lines[line] != "\n":
        rules.append(lines[line].strip())
        line += 1
    line += 1
    while line < len(lines):
        updates.append(list(map(int, lines[line].split(","))))
        line += 1

    if DEBUG:
        print(f"Dataset: {filename}")
        print(f"rules: {rules}")
        print(f"updates: {updates}")



def sort_using_rules(first, second):

    for rule in rules:
        [pre, post] = list(map(int, rule.split("|")))
        # reverse order if we find a rule violation
        if second == pre and first == post:
            return 1
        # short-circuit if we find a matching rule we pass  
        elif first == pre and second == post:
            return -1
    result = 0 if first == second else -1
    return result

def update_follows_rules(update):
    sorted_update = sorted(update, key=functools.cmp_to_key(sort_using_rules))
    return update == sorted_update

def middle_page(update):
    return update[(len(update) // 2)]

def sum_of_middle_pages(updates):
    return sum(middle_page(update) for update in updates)


updates_following_rules = []
sorted_updates_breaking_rules = []

def process_updates():
    updates_following_rules.clear()
    sorted_updates_breaking_rules.clear()

    for update in updates:
        sorted_update = sorted(update, key=functools.cmp_to_key(sort_using_rules))
        if update == sorted_update:
            updates_following_rules.append(update)
        else:
            sorted_updates_breaking_rules.append(sorted_update)


def part_one():
    return sum_of_middle_pages(updates_following_rules)

def part_two():
    return sum_of_middle_pages(sorted_updates_breaking_rules)



# Unit Testing with test data from the statement
load_data(statement_datafile)
process_updates()

assert(middle_page([75,47,61,53,29]) == 61)
assert(middle_page([97,61,53,29,13]) == 53)
assert(middle_page([75,29,13]) == 29)
assert(sum_of_middle_pages([[75,47,61,53,29], [97,61,53,29,13], [75,29,13] ]) == 143)          

assert(sorted([75,97,47,61,53], key=functools.cmp_to_key(sort_using_rules)) == [ 97, 75, 47, 61, 53 ])

assert(update_follows_rules(updates[0]) == True)
assert(update_follows_rules(updates[1]) == True)
assert(update_follows_rules(updates[2]) == True)
assert(update_follows_rules(updates[3]) == False)
assert(update_follows_rules(updates[4]) == False)
assert(update_follows_rules(updates[5]) == False)


assert(part_one() == 143)
assert(part_two() == 123)


# Run solution with real data file
load_data(solve_datafile)
process_updates()
part_one_result = part_one()
assert(part_one_result == 6041)
part_two_result = part_two()
assert(part_two_result == 4884)

