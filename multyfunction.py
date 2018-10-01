#sprogram for simple calculator
i=int(input("enter the value of i:"))
j=int(input("enter the value of j:"))
o=input("what do u want to perform? +,-,*,/:")
def add():
	return i+j
def sub():
	return i-j
def mult():
	return i*j
def division():
	return i/j
if(o=='+'):
	print("addidtion=",add())
elif(o=='-'):
	print("subtraction=",sub())
elif(o=='*'):
	print("multiplycation=",mult())
elif(o=="/"):
	print("devision=",division())

		

