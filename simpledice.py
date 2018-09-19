#write a program to print random numbers specifing r to roll the dice
import random
while True:
	a=input("press 'r' to roll the dice,'q' to quit")
	if(a=='r'):
		print(random.randint(1,6))
	elif(a=='q'):
		print("bye!")
		break
	else:
		print("give either 'r' or 'q'")


