
def load_data(filename, data_type=None):
	with open(filename, 'r') as fp:

		if data_type:
			return [data_type(x) for x in fp.readlines()]
		else:
			return fp.readlines()