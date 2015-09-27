from random import randint
class Game:
	def __init__(self):
		self.player_list = []
		self.turn_score = 0
		self.max_turns = 0
		self.turn_counter = 0
		self.win_score = 0
		self.setup()

	def setup(self):
		players = int(input('How many people are playing? :'))
		self.max_turns = int(input('How many turns will this game last? :'))
		self.win_score = int(input('What is the target score for this game? :'))
		while len(self.player_list) < players:
			add_player()
			if len(self.player_list) == players
			break

	def play(self):
		current = 0
		turn_over = False
		while self.is_game_over == False
			while turn_over == False
				choice = self.turn_menu()
				if choice == 0:
					self.outcomes(self.roll())
				elif choice == 1:
					print(self.get_scores())
				elif choice == 2:
					self.end_turn()

	def add_player(self):
		name = input('Player Name: ')
		if name in player_list[]:
			return False
		else:
			player_list.append.(Player(name))

	def get_scores(self):
		order = sorted([idx.name, idx.score]: for idx in player_list(key=lambda item:item[1]))
		return order

	def roll(self):
		di_1 = randint(1,6)
		di_2 = randint(1,6)
		return di_1, di_2

	def is_game_over(self):
		if self.turn_counter == self.max_turns:
			return True
		order = self.get_scores()
		for i in order:
			if order[i][1] == self.win_score
				return True
		return False

	def turn_menu(self):
		while 1 == 1:
			print('0-Roll Dice, 1-check scores, 2-end turn')
			choice = int(input('Please enter your selection: '))
			if choice not in (0,1,2):
				print('Your selection is invalid')
			else:
				return choice

	def outcomes(self, result):
		if result[0] == 1 and result[1] ==1:
			print('DOUBLE PIG! Your score is reset to 0!')
			self.player_list[current].reset_score()
		elif result[0] == 1 or result[1] == 1:
			print('PIG! Your turn score is reset to 0!')
			self.turn_score = 0
		elif result[0] == result[1]:
			print('DOUBLES! Reroll the dice.')
		else:
			#self.turn_score += sum(result)
			print('Your turn score has been increased by {}').format(sum(result))

	def add_score(self):
		self.player_list[current].add_score(self.turn_score)

	def end_turn(self):
		print('{} ends their turn.').format(str(player_list[current].name))
		self.turn_score = 0
		current += 1
		if current not in range(0, len(player_list)-1):
			current = 0