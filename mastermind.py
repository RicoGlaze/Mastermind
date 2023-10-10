import getch
import random
import os
import time

DEFAULT_HEIGHT=6
WIDTH=4
turn=0
pos_y=0
unlocked=False
game_on=True
BLUE='\33[1;34;40m'
RED='\33[1;31;40m'
PURPLE='\33[1;35;40m'
GREEN='\33[1;32;40m'
NORMAL='\33[0m'
NEGATIVE='\33[3;37;40m'
WHITE='\33[1;37;40m'
BLACK='\33[1;30;40m'
DARK_BLACK='\33[0;30;40m'
UNDERLINE='\33[4m'
CPEG='¤'
KPEG='•'
shades=[BLUE,RED,PURPLE,GREEN,WHITE]
#-------------------------CLASSES-----------------------------------
class Peg:
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color
	def Line(self,dx,dy):
		board[dx][dy].char=UNDERLINE+board[dx][dy].char+NORMAL
	def Color(self,dx,dy,shade):
		board[dx][dy].color=shade
	def Reset(self,dx,dy):
		board[dx][dy].char = CPEG
		
class Code:
	def __init__(self,char,color):
		self.char=char
		self.color=color
	def RandomColor(self):
		self.color=random.choice(shades)
#-------------------------FUNCTIONS-------------------------------
def make_code():
	global code
	code=[Code('¤',WHITE)
	    for i in range(4)]   
	for j in range(4):
		code[j].RandomColor()
		print(code[j].color+code[j].char+NORMAL)
		
def make_codePegs():
	global board
	board=[[Peg(0,0,'¤',BLACK)
		for y in range(WIDTH)]
			for x in range(DEFAULT_HEIGHT)]
			
def make_keyPegs():
	global keys
	keys=[[Peg(0,0,'•',DARK_BLACK)
		for y in range(WIDTH)]
			for x in range(DEFAULT_HEIGHT)]

def checkCode():
	global turn
	for i in range(4):
		for j in range(4):
			if board[turn][j].color==code[j].color:
				keys[turn][j].color=BLACK
			elif code[j].color==board[turn][i].color:
				keys[turn][i].color=WHITE
	turn=turn+1

def checkKeys(unlocked):
	#global unlocked
	if keys[turn-1][0].color==BLACK and keys[turn-1][1].color==BLACK and keys[turn-1][2].color==BLACK and keys[turn-1][3].color==BLACK:
		unlocked = True
		return unlocked
			
def handle_keys():
	global pos_y
	global CPEG
	key=getch.getch()
	#movement keys
	if key=='a' and pos_y>0:
		board[turn][pos_y].Reset(turn,pos_y)
		pos_y=pos_y-1
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='d' and pos_y<3:
		board[turn][pos_y].Reset(turn,pos_y)
		pos_y=pos_y+1
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='b':
		board[turn][pos_y].Color(turn,pos_y,BLUE)
		board[turn][pos_y].Reset(turn,pos_y)
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='r':
		board[turn][pos_y].Color(turn,pos_y,RED)
		board[turn][pos_y].Reset(turn,pos_y)
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='p':
		board[turn][pos_y].Color(turn,pos_y,PURPLE)
		board[turn][pos_y].Reset(turn,pos_y)
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='g':
		board[turn][pos_y].Color(turn,pos_y,GREEN)
		board[turn][pos_y].Reset(turn,pos_y)
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='w':
		board[turn][pos_y].Color(turn,pos_y,WHITE)
		board[turn][pos_y].Reset(turn,pos_y)
		board[turn][pos_y].Line(turn,pos_y)
	elif key=='\n':
		checkCode()
			
def render_all():
	print('Color Key:'+RED+' R=Red,'+BLUE+' B=Blue,'+GREEN+' G=Green,'+WHITE+' W=White,'+PURPLE+' P=Purple'+NORMAL)
	print('Movement Left/Right: A/D')
	print('Check code: Enter key')
	print('\n' +' '*16+'MASTERMIND')
	print(' '*12+'_'*18)
	for i in range(DEFAULT_HEIGHT):
		print(' '*12+'{',end='')
		for j in range(WIDTH):
			print(board[i][j].color+board[i][j].char+NORMAL,end='')
			print(end='}{')
		for x in range(WIDTH):
			print(keys[i][x].color+keys[i][x].char+NORMAL,end='')
		print('}')

def underline_position():
	board[turn][pos_y].Line(turn,pos_y)
	board[turn][pos_y].Reset(turn-1,pos_y)
	
def end_Game():
	print('You guessed the code in '+str(turn)+' turns.')
	time.sleep(3)
	
def keep_playing():
	answer='y'
	print('\nPlay again? Y/N')
	answer = input()
	if answer=='y' or answer=='Y':
		game_on=True
		return game_on
	else:
		game_on=False
		return game_on
#-------------------------MAIN-----------------------------------------
while game_on==True:
	turn=0
	make_codePegs()
	make_keyPegs()
	make_code()
	while turn!=6:
		os.system('cls')
		underline_position()
		render_all()
		handle_keys()
		unlocked=checkKeys(unlocked)
		os.system('cls')
		render_all()
		if unlocked==True:
			break
	if unlocked==True:
		end_Game()
	else:
		print('You failed to guess the code within '+str(DEFAULT_HEIGHT)+' attempts.')
		time.sleep(3)
	game_on=keep_playing()
