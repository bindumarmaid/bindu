#write a program for rock,paperand sizer
import random
p={1:'r',2:'p',3:'s'}
count1=0
count2=0
while True:
	yourchoice=input("YOU CHOICE:r/p/s:")
	computerchoice=p[random.randint(1,3)]
	print("your choice",yourchoice,"computer choice",computerchoice)
	if(yourchoice=='r'or yourchoice=='s' or yourchoice=='p'):
		if(yourchoice==computerchoice):
			print("tie !!")
		elif(yourchoice=='s' and computerchoice=='r' or yourchoice=='r' and computerchoice=='p' or yourchoice=='p' and computerchoice=='s'):
			count1=count1+1
			print("computer won!!",count1,"times")
		else:
			count2=count2+1
			print("you won!!",count2,"times")
	else:
		print("give proper input")
		break
	if(count1==3 or count2==3):
		if(count1==3):
			print("sorry computer won the game!:")
		else:
			print("congratulation u won the game!!:")
		break



