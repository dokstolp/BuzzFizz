import math


# Ask for the input for the program, and make sure it is in acceptable format
def startup():
	inputValue = raw_input("How many numbers of the Fibonacci sequence would you like: ")
	if inputValue.isdigit() == False: # in case the user gives the inputValue as something other than an intiger
		print("Input must be a positive integer")
		startup()
	else:
		Fibonacci(int(inputValue))

# Loops over the range for n and calculates the nth Fibonacci number
def Fibonacci(n):
	vers = [0,1]
	for i in range(1,n+1):
		if i<=78: # Closed form works up until the 78th Fibonacci number, afterwards this equation has only even numbers (not correct)
			fib_i = ((1+math.sqrt(5))**i-(1-math.sqrt(5))**i)/(2**i*math.sqrt(5))# Taken from Wolfram http://mathworld.wolfram.com/FibonacciNumber.html
			if i>76:
				vers[i%2-1]= int(fib_i)
		else:# After 78 the sequence must be calculated sequentially
			fib_i = vers[i%2]+vers[i%2-1]			
			vers[i%2-1]= fib_i
		print(outputValue(int(fib_i)))# Printing the output of the "Buzz/Fizz" 
		
# Provides the output in case the Fibonacci number is even or divisable by 3,5 or 15.
def outputValue(p):
	outputs = ["Buzz","Fizz","FizzBuzz"]
	m = -1
	if p==1 or p%2==0:# if the number is divisable by two it is automatically not "Buzz/Fizz" worthy
		return p
	if p%3==0:
		m = 0
	if p%5 ==0:
		if m==0:
			m=2# if it is divisable by 3 and 5 it must be divisable by 15
		else:
			m=1
	if m>=0:
		return outputs[m]
	return isPrime(p)

# Checks if the number is prime
def isPrime(p):
	isPrime = True
	for v in range(7,int(math.sqrt(p)),2):# 7 is used for minimum because that is the next possible prime number > 5.
		if p%v == 0:
			isPrime = False
			break
	if isPrime == True:
		return "BuzzFizz"
	else:
		return p

		
#begin program
startup()
