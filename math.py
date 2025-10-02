#code for journal one, session 2
#print the sum of two floating numbers
#print the difference between two integers
#print the product of a floating point number and an integer
#print out the data type of each answer

def add(x, y):
	return x + y
		
def subtract(x, y):
	return x - y

def multiply (x, y):
	return x * y

def main():
	a = 1.0
	b = 2.0
	c = 3
	d = 4

	print(add(a, b))
	print(type(add(a, b)))

	print(subtract(c, d))
	print(type(subtract(c, d)))

	print(multiply(a, c))
	print(type(multiply(a, c)))

if __name__=="__main__":
	main()