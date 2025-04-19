#Ask the user for a number. Print whether it's positive, negative, or zero.
"""number=int(input())

if(number<0):
    print(number,"is less than zero, negative number")
elif(number>0):
    print(number,"is greater than zero positive number")
else:
    print("the given ",number,"is equal to zero")"""


#Ask the user for a number and check if it's even or odd.

number=int(input())
calc=number%2
#print(calc)
if(number==0):
    print("given number is Zero")
elif(calc):
    print(number,"is odd")
else:
    print(number,"is even")