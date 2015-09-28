class Player:
	def __init__(self, name=None):
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

# class AI(Player):
# 	self.risk_rating = 0
# 	def risk(self, scores, win_score, max_turns, turn_counter):
# 		score_leader = (max(scores), key=lambda i: i[1]))
# 		score_loser = (min(scores), key=lambda i: i[1]))
# 		score_percent = (score_leader[1] * 100) // win_score
# 		turn_percent = (turn_counter * 100) // max_turns
# 		#lead_percent = (next closest score * 100) // super.score
# 		deficit_percent = (super.score * 100) // score_leader[1]
# 		if score_leader[0] == super.name:
# 			self.risk_rating -= 1
# 		if score_leader[0] != name