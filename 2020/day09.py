# Solution to Advent of Code 2020, day 9
# https://adventofcode.com/2020/day/9
from util import load_data

DEBUG_PART_ONE = False
DEBUG_PART_TWO = False

class Xmas():

	# preamble is an array of ints
	def __init__(self, preamble_size, data):
		self.preamble_size = preamble_size
		self.preamble = data[0:preamble_size]
		self.remaining_data = data[preamble_size:]
		self.index = preamble_size

		# if DEBUG_PART_ONE or DEBUG_PART_TWO:
		# 	print(f"Preamble: {self.preamble}")
		# 	print(f"Remaining Data: {self.remaining_data}")

	def advance_data(self):
		self.index += 1
		self.preamble.pop(0)
		self.preamble.append(self.remaining_data.pop(0))

	def find_vulnerability(self, data, target):

		index = 0
		sequence = [data.pop(0)]

		while len(data) > 0:
			
			sequence.append(data.pop(0))
			while sum(sequence) > target:
				sequence.pop(0)

			if sum(sequence) == target and len(sequence) > 1:
				if DEBUG_PART_TWO:
					print(f"Found sequence summing target {target} : {sequence}")
				sequence.sort()
				return sequence[0] + sequence[-1]


	def find_invalid_number(self):
		while len(self.remaining_data) > 0:

			if not self.test_next_item():
				return self.remaining_data[0]

			self.advance_data()

		return None

	def test_next_item(self):
		if DEBUG_PART_ONE:
			print(f"* Testing {self.remaining_data[0]} against preamble {self.preamble}")

		for preamble_member in self.preamble:

			if self.remaining_data[0] - preamble_member in self.preamble:
					return True

			if DEBUG_PART_ONE:
				print(f"Determined that {self.remaining_data[0]} - {preamble_member} = {self.remaining_data[0] - preamble_member} is not in preamble")

		return False

def test_data():
	data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
	xmas = Xmas(preamble_size=5, data=data)
	result = xmas.find_invalid_number()
	print(f"Test find_invalid_number returns: {result}")
	assert(result == 127)

	xmas = Xmas(preamble_size=5, data=data)
	result = xmas.find_vulnerability(data=data, target=result)
	print(f"Test find_vulnerability returns: {result}")
	assert(result == 62)

def part_one():
	data = load_data('Data/day09.txt', data_type=int)
	xmas = Xmas(preamble_size=25, data=data)
	result = xmas.find_invalid_number()
	print(f"Part one returns: {result}")	

def part_two():
	data = load_data('Data/day09.txt', data_type=int)
	xmas = Xmas(preamble_size=25, data=data)
	target = xmas.find_invalid_number()
	result = xmas.find_vulnerability(data=data, target=target)
	print(f"Part two returns: {result}")		

test_data()
part_one()
part_two()

