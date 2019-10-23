#!/bin/python3

##################################################################################
##																				##
##									#Python3									##
##							#This is a little 101 Script for Python3			##
##								#2019 written by rwx777							##
##																				##
####################################################################################

#Print strings
print("Hek the police")
print ("Hek" + "something")

#Print new line
print("\n")

################################################################################

#Math
print("Math Time")
print(77 + 77) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovers

print("\n") #new line

################################################################################

#Variables & Methodes

print("Fun with varibales and methods:")
quote = "Hacking is fun if youre a Hacker"
print(len(quote)) #length of quote
print(quote.upper()) #makes quote uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title makes everyfirst letteler captial

name = "Elliot"
age = 23 #int int(23)
abi = 3.2 #float float(3.2)

print(int(age))
print(int(23.8)) # does not round

print("My Name is " + name + " and I am " + str(age) + " years old.") #nice

print("\n") #new line

age += 1
print(age) #now is 24

birthday = 1
age += birthday
print(age) #now 25

################################################################################

#Functions
print("Now, some functions:")
def who_am_i():
	name = "Elliot"
	age = 23 #int int(23)
	print("My Name is " + name + " and I am " + str(age) + " years old.") #nice
	#variables delcared in function are only avidlble in function

who_am_i() #called function

#adding in parameters
def add_one_hundred(num):
	print(num + 100)
	#mini programm

add_one_hundred(50)
# will give us 150

#add in multiply parameters
def add(x,y):
	print(x + y)

add(7,7) #adds 7+7 cus of the function we wrote
add(305,207) #adds 305 + 207

#using return
def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	return x ** .5

print(square_root(64))

def new_line():
	print("\n") #new line

new_line()

################################################################################

#boolean expressions (True or false)
print("Boolean expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True" #its a trap
print(type(bool5))

#################################################################################

#Relational und Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7>5) and (5>7) # True & True returns True
test_or = (7>5) or (5<7)
test_not = not True #is False
#check Truth Tables

new_line()

################################################################################

#Conditional Statments
print("Conditional Statments:")
def soda(money):
	if money >= 2:
		return "You have got a Soda!"
	else:
		return "NO Soda for you!"

print(soda(3))
print(soda(1))

def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "Lets get Wasted!"
	elif(age >= 21) and (money < 5):
		return "You broke homi3!"
	elif(age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "Youre too poor and too young"

print(alcohol(19,100))
print(alcohol(23,3))
print(alcohol(90,10))

new_line()

################################################################################

#Lists
print("LISTS have brackets:")
movies = ["Wall-E","The Great Gatsby","The Perks of being a Wallflower"]

print(movies[0]) #Lists start a 0 like arrays
print(movies[0:2]) #prints the first and the second item
print(movies[1:]) #up to but not encluding/ prints all movies from second to last
print(movies[:1]) #from to first to second
print(movies[-1]) #negative one gets last item from list
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop() #removes last item in List
print(movies)

person = ["Hannah","Clay","Zack"]

combined = zip(movies,person) #combines 2 lists
print(list(combined))

################################################################################

#Tuples
print("Tuples have paranthesis and cannot change") #static bzw imutable
grades = ("A", "B", "C", "D", "F")
print(grades[1])

new_line()

################################################################################

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber","spinach","cabbage"]
for x in vegetables:
	print(x)

print("While loops - Execute as long as True:")
i = 1
while i < 10:
	print(i)
	i += 1
	#counts up to 10
