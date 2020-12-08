# Solution to Advent of Code 2020, day 8
# https://adventofcode.com/2020/day/8
from util import load_data

DEBUG = False
OP_ACCUMULATE = 'acc'
OP_JUMP = 'jmp'
OP_NOP = 'nop'

class handheldConsole():
	# program is a list of strings, each containing one operation
	def __init__(self, program, attempt_repair=False):
		self.accumulator = 0
		self.code_offset = 0
		self.program = program
		self.visited_offsets = []
		self.repair_offset = -1
		self.attempt_repair = attempt_repair

	def run(self):

		self.visited_offsets.append(self.code_offset)

		while self.code_offset < len(self.program):
			self.execute_step()

			if not self.have_we_visited(self.code_offset):
				self.visited_offsets.append(self.code_offset)
				continue

			# Endless loop was detected

			# Code to handle part one where we don't try to repair the program
			if not self.attempt_repair:
				print(f"Endless loop detected at offset: {self.code_offset}.")
				return self.accumulator

			# Code for part two- attempting to repair the program:

			# Reset the program and try repairing the next offset
			self.accumulator = 0
			self.code_offset = 0
			self.visited_offsets = []

			self.repair_offset += 1

			if DEBUG:
				print(f"Endless loop detected at offset: {self.code_offset}. Trying to repair {self.repair_offset}")

		if DEBUG and self.repair_offset:
			print(f"Program repaired by repairing: {self.repair_offset} ({self.program[self.repair_offset].strip()})")

		return self.accumulator

	def execute_step(self):
		command = self.program[self.code_offset]
		value = int(command.split(' ')[1].strip())
		operation = command.split(' ')[0].strip()

		# If we're in repair mode and this command is the next candidate
		# we'll swap jmp and nop
		if self.repair_offset == self.code_offset:
			if operation == OP_JUMP:
				operation = OP_NOP
			elif operation == OP_NOP:
				operation = OP_JUMP
			else:
				# Run the accumulator operation normally and make 
				# the next operation the repair candidate
				self.repair_offset += 1

		if operation == 'acc':
			self.accumulator += value
			self.code_offset += 1
		elif operation == OP_JUMP:
			self.code_offset += value
		elif operation == OP_NOP:
			self.code_offset += 1
		else:
			print(f'Unsupported command: {command}')

		# print(f"Operation: {operation}\tValue: {value}\tAccumulator: {self.accumulator}")

	def have_we_visited(self, offset):
		return offset in self.visited_offsets


def test_data():
	data = """nop +0
		acc +1
		jmp +4
		acc +3
		jmp -3
		acc -99
		acc +1
		jmp -4
		acc +6""".split('\n')

	console = handheldConsole(data)
	result = console.run()
	print(f"Test run returns: {result}")
	assert(result == 5)

def part_one():
	data = load_data('Data/day08.txt')
	console = handheldConsole(data)
	print(f"Part one returns: {console.run()}")	

def part_two():
	data = load_data('Data/day08.txt')
	console = handheldConsole(data, attempt_repair=True)
	print(f"Part two returns: {console.run()}")		

test_data()
part_one()
part_two()

