#write a program to play the snake and ladder game
import random
count=0
def myroll():
	return random.randint(1,6)
while (count<=100):
	a=input("press 'r' to roll the dice,'q' to quit")
	if(a=='r'):
		r=myroll()
		count=count+r
		print("u got",r)
		print("new position is",count)
	elif(count==8):
		count=37
		print("congrats!u climed the lader")
	elif(count==11):
		count=2
		print("sorry!u got the snake")
	elif(count==13):
		count=34
		print("congrats!u climed the lader")



	elif(a=='q'):
		print("bye!")
		break
		
	else:
		print("give either 'r' or 'q'")
