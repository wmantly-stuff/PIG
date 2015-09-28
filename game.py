from random import randint
from player import Player

class Game:
	def __init__(self):
		self.player_list = []
		self.turn_score = 0
		self.max_turns = 0
		self.turn_counter = 0
		self.win_score = 0
		self.turn_over = False
		self.current = 0
		self.setup()

	def setup(self):
		players = int(input('How many people are playing? :'))
		fair = False
		while fair == False:
			self.max_turns = int(input('How many turns will this game last? :'))
			if self.max_turns % players != 0:
				print('with this setting the players will not an have equal number of turns')
			else:
				fair = True
		self.win_score = int(input('What is the target score for this game? :'))
		while len(self.player_list) < players:
			self.add_player()
			if len(self.player_list) == players:
				break
		self.play()

	def play(self):
		self.current = 0
		while self.is_game_over() == False:
			self.turn_over = False
			while self.turn_over == False:
				choice = self.turn_menu()
				if choice == 0:
					self.outcomes(self.roll())
				elif choice == 1:
					print(self.get_scores())
				elif choice == 2:
					self.end_turn()

		print(max(self.get_scores(), key=lambda i: i[1]))
		print('Wins the game!')
		play_again = input('would you like to play again?(Y/n) ')
		if play_again == 'n':
			exit()
		if play_again == 'Y':
			game = Game()

	def add_player(self):
		name = input('Player Name: ')
		if name in self.player_list:
			return False
		else:
			self.player_list.append(Player(name))

	def get_scores(self):
		order = sorted([ (idx, pl.name, pl.score) for idx,pl in enumerate(self.player_list) ], key=lambda item:item[2])
		return order

	def roll(self):
		di_1 = randint(1,6)
		di_2 = randint(1,6)
		return di_1, di_2

	def is_game_over(self):
		if self.turn_counter == self.max_turns:
			return True
		order = self.get_scores()
		# print(order)
		for i in order:
			if i[2] >= self.win_score:
				return True
		return False

	def turn_menu(self):
		while 1 == 1:
			print('{} has the dice'.format(self.player_list[self.current].name))
			print('0-Roll Dice, 1-check scores, 2-end turn')
			choice = int(input('Please enter your selection: '))
			if choice not in (0,1,2):
				print('Your selection is invalid')
			else:
				return choice

	def outcomes(self, result):
		if result[0] == 1 and result[1] ==1:
			print('DOUBLE PIG! Your score is reset to 0!')
			self.player_list[self.current].reset_score()
			self.end_turn()
		elif result[0] == 1 or result[1] == 1:
			print('PIG! Your turn score is reset to 0!')
			self.turn_score = 0
			self.end_turn()
		elif result[0] == result[1]:
			print('DOUBLES! No change to turn score. Reroll the dice.')
		else:
			roll_score = sum(result)
			self.turn_score += roll_score
			print('Your turn score has been increased by {}'.format(sum(result)))

	def add_score(self):
		self.player_list[self.current].add_score(self.turn_score)

	def end_turn(self):
		print('{} ends their turn.'.format(str(self.player_list[self.current].name)))
		if self.turn_score > 0:
			self.add_score()
		self.turn_score = 0
		self.current += 1
		if self.current not in range(0, len(self.player_list)):
			self.current = 0
		self.turn_over = True
		return

#planned improvements include:
#showing turn score
#show scoreboard every turn
#show the turn number
#finish the AI