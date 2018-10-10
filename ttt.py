#write a program for tic tac toe
a=['1','2','3','4','5','6','7','8','9']
def printBoard():
	print('\n--------')
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print('-----------')
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print('-----------')
	print('|',a[6],'|',a[7],'|',a[8],'|')
	print('---------\n')
p1=True
while(True):
	printBoard()
	if p1:
		p=input("player1,choose your place:")
		if p in a:
			a[int(p)-1]='x'
			p1=not p1
	else:
		p=input("player2,choose your place:")
		if p in a:
			a[int(p)-1]='o'
			p1=not p1
#checking for rows
	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			print("game over!!!")
			printBoard()
			exit()
#checking for columns
	for i in (0,1,2):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			print("game over!!!")
			if (a[i]=='x'):
				print("player1 won the game!!")
			else:
				print("player2won the game!!")
			printBoard()
			exit()
#checking for diagonal(l to r)
		if(a[0]==a[4] and a[0]==a[8]):
			print("game over!!!")
			if (a[4]=='x'):
				print("player1 won the game!!")
			else:
				print("player2won the game!!")
			printBoard()
			exit()			
#checking for diagonal(r to i)
		if(a[2]==a[4] and a[2]==a[6]):
			print("game over!!!")
			if (a[4]=='x'):
				print("player1 won the game!!")
			else:
				print("player2won the game!!")
			printBoard()
			exit()	
		




