class Player:
	__init__(self, name):
	self.name = name
	self.score = 0

	def add_score(self, turn):
		self.score += turn

	def reset_score(self):
		self.score = 0

	def display_name(self):
		return self.name

	def display_score(self):
		return self.score 
