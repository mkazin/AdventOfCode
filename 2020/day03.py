# Solution to Advent of Code 2020, day 3
# https://adventofcode.com/2020/day/3
from util import load_data

SQUARE_OPEN = '.'
SQUARE_TREE = '#'

class tobogganPath():

	def __init__(self, slope_right, slope_down, map):
		self.slope_right = slope_right
		self.slope_down = slope_down
		self.map = map
		self.pos_x = 0
		self.pos_y = 0
		self.tree_count = 0

	def width(self):
		return len(self.map[0])

	def height(self):
		return len(self.map)

	def advance_position(self):

		new_x = self.pos_x + self.slope_right
		if new_x >= self.width():
			self.pos_x = new_x % self.width()
		else:
			self.pos_x = new_x

		self.pos_y += self.slope_down

		if not self.at_bottom() and self.is_current_position_tree():
			self.tree_count += 1

		# print(f"({self.pos_x},{self.pos_y}) => {self.map[self.pos_y][self.pos_x]} , trees = {self.tree_count}")

	def is_current_position_tree(self):
		return self.map[self.pos_y][self.pos_x] is SQUARE_TREE

	def at_bottom(self):
		return self.pos_y >= self.height()

def part_one():
	print("\n*** Part One ***\n")
	toboggan = tobogganPath(slope_right=3, slope_down=1, map=MAP)
	while not toboggan.at_bottom():
		toboggan.advance_position()

	print(f"Trees encountered: {toboggan.tree_count}")

def part_two():
	print("\n*** Part Two ***\n")
	slopes = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
	result = 1

	print("Iterating over slopes:")
	for slope_right, slope_down in slopes:
		toboggan = tobogganPath(slope_right=slope_right, slope_down=slope_down, map=MAP)
		while not toboggan.at_bottom():
			toboggan.advance_position()

		print(f"- Tree count: {toboggan.tree_count}")
		result *= toboggan.tree_count

	print(f"\nProduct of these: {result}")

MAP = load_data('Data/day03.txt')

part_one()
part_two()
