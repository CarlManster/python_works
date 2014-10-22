import math

def drawLine(): print("--------------------")
	
def sort(a, b):
	if a > b: temp = a;a = b;b = temp
	return a, b
	
def showNum(a, b):
	c, d = sort(a, b)
	while c <= d: print(c);c = c + 1
	drawLine()
	
def printLoop(a):
	if type(a) is not str and type(a) is not dict and type(a) is not list:
		print('%s (0)o' % (a))
	else :
		for x in a:
			if type(a) is dict: print('%s (%s)v' % (x, a[x]))
			elif type(x) is str: print('%s (%s)c' % (x, len(x))) 
			elif type(x) is int: print('%s (%s)i' % (x, intLen(x)))
			else: print(x)
	drawLine()
			
def intLen(a):
	digit = 1.0
	if a != 0: digit = math.floor(math.log10(abs(a))) + 1
	return int(digit)

def variTest1():
	print("variTest1")
	global vari
	vari = 10.0
	drawLine()
	
def variTest2():
	try: print("variTest2");print(vari);
	except NameError: print("vari is undefined");
	else: print("vari is defined");
	drawLine()
	
def gender(x):
	if x:
		return "Male"
	return "Female"
	
def mapSquaredRange(x, y):
	return map(lambda z : z ** 2, range(x, y))
	
def mapSquaredRangeFromZero(x):
	return mapSquaredRange(0, x)
	
def reduceComparedRange(x, y):
	return reduce(lambda a, b : a if a > b and a % 3 == 0 else b, range(x, y))

def reduceComparedRangeFromZero(x):
	return reduceComparedRange(0, x)
	
def filterOddRange(x, y):
	return filter(lambda a : a % 2 == 1, range(x, y))
	
def filterOddRangeFromZero(x):
	return filterOddRange(0, x)

def makeComplex(a, b):
	return complex(a+b*1j)

comp1 = complex(10.0+7.2j)
comp2 = complex(2.0+2.6j)
comp3 = makeComplex(1.7, 2.9)
family = ["grand father", "grand mother", "father", "mother", "son", "daughter"]
person = {"name" : "Carl", "age" : 33, "male" : True, "lat" : 38.537798, "lon" : 126.835636}
numbers = range(-120, 120, 37)

drawLine()

print('Hello Python World.')
print('%s & %s' % (family[2], family[3]))
print('%s is %s-year-old %s.' % (person["name"], person["age"], gender(person["male"])))
print('%s + %s = %s' % (comp1, comp2, comp1 + comp2))
print('%s + %s = %s' % (comp1, comp3, comp1 + comp3))
print(numbers)
print(person)

drawLine()

variTest2()
variTest1()
variTest2()

printLoop(family)
printLoop(numbers)
printLoop(person)
printLoop("Hello World")
printLoop(mapSquaredRangeFromZero(15))
printLoop(mapSquaredRange(30, 35))
printLoop(reduceComparedRangeFromZero(105))
printLoop(reduceComparedRange(30, 35))
printLoop(filterOddRangeFromZero(20))
printLoop(filterOddRange(50, 74))
showNum(40, 45)
showNum(70, 67)
