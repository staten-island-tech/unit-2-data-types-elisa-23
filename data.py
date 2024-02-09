#Data Types
#Numbeers 1,2,3
""" def add(x,y):
    print(x+y)
add(1,2)
#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same
add("1","2")
#undefined/null

#booleans
tenure = False
def is_tenured(status):
    if(status==true):
        print("They have tenured")
    else:
        print("they are not tenured") """
    
""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

#Word Counter
""" def wordcounter():
    x = input("Enter a Statement: ")
    y = x.split( )
    words = 0
    for i in y:
        words += 1
    print(words)
wordcounter() """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
#this code would print the word "warm"

#Determines if the number is even or odd
""" def evenorodd():
    number = float(input("Enter your number:"))
    x = number % 2
    if x == 0:
        print('the number is even')
    elif x == 1:
        print('the number is odd')
evenorodd() """

""" factor = [1]
def factors():
    number = int(input("Enter your number:"))
    factor.append(number)
    y = 1
    for i in range(number):
        y += 1
        if number % y == 0:
            factor.append(y)
            factor.append(number/y)
        else:
            y += 1
            number % y
    print(f"Factor:{factor}") """

factor1 = [1]
factor2 = []
def gcf():
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))
    y = 1
    for i in range(number1):
        y += 1
        if number1 % y == 0:
            if number2/y == 0:
                if y>factor2[1]:
                    factor2 = []
                    factor2.append(y)
            if number2/(number1/y) == 0:
                if (number1/y)>factor2[1]:
                    factor2 = []
                    factor2.append(number1/y)
        else:
            y += 1
            number1 % y
    print(f"GCF;{factor2[1]}")
gcf()