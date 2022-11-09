import random
class Game:
	def __init__(self):
		self.board = [[None for i in range(3)] for j in range(3)]
		mark1 = 'X'
		mark2 = 'O'
		
	
	def init_board(self):
		tile = 0
		for i in range(3):
			for j in  range(3):
				self.board[i][j]=tile
				tile +=1

	def is_empty(self,tile):
		i = tile//3
		j = int(tile%3)
		if self.board[i][j] != 'X' and self.board[i][j] != 'O':
			return True
		return False
	
	def player_move(self,tile,mark):
		i = tile//3
		j = int(tile%3)
		self.board[i][j] = mark

	def check_if_win(self,last_move=None):
		if last_move is None:
			return False
		i = last_move//3
		j = int(last_move%3)
		return self.check_row(i,j) or self.check_column(i,j) or self.major_diagonal() or self.minor_diagonal()

	def check_row(self,x,y):
		mark = self.board[x][y]
		for j in range(3):
			if self.board[x][j] != mark:
				return False
		return True

	def check_column(self,x,y):
		mark = self.board[x][y]
		for j in range(3):
			if self.board[j][y] != mark:
				return False
		return True

	def major_diagonal(self):
		mark = self.board[1][1]
		for i in range(3):
			if self.board[i][i] != mark:
				return False
		return True
				

	def minor_diagonal(self):
		mark = self.board[1][1]
		for i,j in zip(range(3),range(2,-1,-1)):
			if self.board[i][j] != mark:
				return False
		return True

	def ai_move(self,mark):
		cornor = [0,8,2,5]
		for tile in cornor:
			if self.is_empty(tile):
				self.player_move(tile,mark)
				return tile
		
		if self.is_empty(4):
			self.player_move(4,mark)
			return 4

		other_tiles = [1,3,5,7]
		for tile in other_tiles:
			if self.is_empty(tile):
				self.player_move(tile,mark)
				return tile

	def multi_player(self):
		print('Player 1 : X\n')
		print('Player 2 : O\n')
		player = None
		num_moves = 0
		while num_moves < 9:
			self.print_board()
			if num_moves % 2 ==0:
				move = int(input('Input tile number,Player 1:'))
				player = '1'
				self.player_move(move,'X')
			else:
				player = '2'
				move = int(input('Input tile number,Player 2:'))
				self.player_move(move,'O')
			if self.check_if_win(move):
				self.print_board()
				print('Winner Player '+player)
				return
			num_moves +=1
		print('It is a Draw')

	def print_board(self):
		for i in range(3):
			print(self.board[i])

	def single_player(self):
		player_mark = input("Enter your mark O/X: ")
		ai_mark = 'X' if player_mark=='O' else 'O'
		toss = random.random()
		flag = True if toss<0.5 else False
		turn = 0
		if flag:print("AI starts")
		else: print("Player starts")
		while turn < 9:
			print("Board : \n")
			self.print_board()
			if flag:
				print("\nAI move")
				tile = self.ai_move(ai_mark)
			else:
				print("\nPlayer move")
				tile = int(input("Player enter your move: "))
				self.player_move(tile,player_mark)
			if self.check_if_win(tile):
				self.print_board()
				if flag:
					print("\nAI WINS!!")
				else:
					print("\nPLAYER WINS!!")
				return
			flag = False if flag else True
			turn+=1
		self.print_board()
		print("IT'S A DRAW")

g = Game()
g.init_board()
# g.multi_player()
g.single_player()
