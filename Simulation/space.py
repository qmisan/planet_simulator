from visual import * # For vectors
class Space(object):
	"""docstring for Space"""
	def __init__(self):
		# Makes space object with given x,y,z size
		self.element_list = []

	def add_element(self,element):
		self.element_list.append(element)

	def calculate_physics(self,time):
		for element in self.element_list:
			element.calculate_next(time)

	def update_physics(self):
		for element in self.element_list:
			element.update()

	def get_smallest(self):
		smallest = self.element_list[0]
		for element in self.element_list:
			if element.mass < smallest.mass:
				smallest = element
		return smallest
	def get_biggest(self):
		biggest = self.element_list[0]
		for element in self.element_list:
			if element.mass > biggest.mass:
				biggest = element
		return biggest

	def get_longest_distance(self):
		longest = self.element_list[0]
		for element in self.element_list:
			if mag(element.position) > mag(longest.position):
				longest = element
		return mag(longest.position)

	def print_elements(self):
		for element in self.element_list:
			print("______________________")
			print(element)
			print("______________________")