import time,os,random

name=["Anaconda","Hippopotamus","Snake","Penguin","Dictionary"]

def pos(string,letter):#Getting the Index of Letter
	for i in range(0,len(string)):
		if string[i]==letter:
			yield i
			
def index(string,letter,chance=1):# Obtaining the List of Index position of Same Letter at Multiple Position
	x=list(pos(string,letter))
	if len(x)<=1:
		return x[0]
	elif len(x)<=chance-1:
		return x[len(x)-1]
	else:
		return x[chance-1]
		
def hangman_title():# ASCII Art of Hangman
	print("""   
█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█""")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def main_game_algo(names):#Main Game Algorithm or Logic
	picks=list(random.choice(names))
	picks1=[]
	for i in picks:
		picks1.append(i)
	shown=list(random.choices(picks,k=len(picks)//2))
	i=0
	while i<len(picks):
		if picks[i] not in shown:
			picks[i]="_"
		i+=1
	print()
	print("            ",f'[ {" ".join(picks)} ]')
	wrong=0
	j=2
	print(HANGMANPICS[wrong])
	while True:
			if picks==picks1:
				print("You won!! :)")
				break
			x=input("Find the Missing Letters : ")
			if x in picks1 and x not in picks:
				picks[picks1.index(x)]=x
			elif x in picks and x in picks1:
				picks[index(picks1,x,j)]=x
				j+=1
			else:
				print(" ! Wrong Letter !")
				time.sleep(1)
				wrong+=1
				if wrong==6:
					os.system("clear")
					print("The Man is Dead , Game Over :(")
					print(HANGMANPICS[wrong])
					break
			os.system("clear")
			hangman_title()
			print()
			print("            ",f'[ {" ".join(picks)} ]')
			print(HANGMANPICS[wrong])

def choice_menus():#Choice Menu
	hangman_title()
	print()
	print("1.Play Game")
	print("2.Add More Word")
	print("3.Help Menu")	
	print("4.Names in the Words")
	print("5.Exit")
	choices=[1,2,3,4,5]
	choice=int(input("Enter Your Choice="))
	if choice not in choices:
		print("Wrong Input!!")
	else:
		return choice

def system_clear():# Making clear screen command
	os.system("clear")
	hangman_title()
	print()
	
def help_game_algo():
	#Main Game Algorithm or Logic
	print(">>>>>THIS VIDEO WILL SHOW YOU HOW TO PLAY<<<<<")

	picks=list(random.choice(name))
	picks1=auto_guess=[]
	for i in picks:
		picks1.append(i)
	shown=list(random.choices(picks,k=len(picks)//2))
	i=0
	while i<len(picks):
		if picks[i] not in shown:
			picks[i]="_"
		i+=1
	picks2=list(random.choice(name))
	picks3=[]
	for z in picks1:
		if z not in shown:
			picks3.append(z)
			
	auto_guess=picks3+list(random.choices(picks2,k=len(picks2)//2))
	random.shuffle(auto_guess)
	hangman_title()
	print()
	print("            ",f'[ {" ".join(picks)} ]')
	wrong=0
	j=2
	print(HANGMANPICS[wrong])
	while True:
			if picks==picks1:
				print("You won!! :)")
				break
			
			x=auto_guess[int(random.random()*len(auto_guess))]
			print(f"Guessed Word is = {x}")
			time.sleep(2)
			if x in picks1 and x not in picks:
				picks[picks1.index(x)]=x
			elif x in picks and x in picks1:
				picks[index(picks1,x,j)]=x
				print("Repeated Guessed Letter")
				time.sleep(2)
				j+=1
			else:
				print(f"{x} is  Wrong Letter, Now See Man Is Starting To Die !")
				print("Everytime You Guess Wrong Letter The Man Will Close to Die!")
				time.sleep(2)
				wrong+=1
				if wrong==6:
					os.system("clear")
					print("The Man is Dead , Game Over :(")
					print(HANGMANPICS[wrong])
					break
			os.system("clear")
			hangman_title()
			print()
			print("            ",f'[ {" ".join(picks)} ]')
			print(HANGMANPICS[wrong])
	
def start_game(): #Starting of Game Function
	ch="y"
	os.system("clear")
	x=choice_menus()
	system_clear()
	if x==1:
		main_game_algo(name)
		ch=input("Want to continue Again ? y/n=")
		if ch=="y":
			return start_game()
	elif x==2:
		ch1="y"
		while ch1!="n":
			word=input("Enter the New Word =")
			if word in name:
				print("This word is already in the list try different new word")
			else:
				name.append(word)
			ch2=input("Want to Try Another Word ? y/n=")
			if ch2=="n" or ch2=='N':
				return start_game()
	elif x==3:
			os.system("clear")
			help_game_algo()
			ch3=input("Want to Watch Again y/n=")
			if ch3!="n":
				help_game_algo()
			else:
				os.system("clear")
				return start_game()
	elif x==4:
		print(f"There are total {len(name)} words in the List \n {name}")
		ch4=input("Want to Goto Main Menu y/n=")
		if ch4!="n":
			return start_game()
	elif x==5:
		print(f"The Total Words is {len(name)} , that are \n {name}")
		ch5=input("Want to Go To Main Menu =")
		if ch5!="n":
			return start_game()
		
	else:
			print("Wrong Input")
			time.sleep(2)
			return start_game()
	print("Bye Bye Come Again To Play")

start_game() # Starting Game.