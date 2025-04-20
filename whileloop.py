"""count=1
while count<=5:
    print("count is",count)
    count +=1"""

#Use a while loop to print "Python is fun!" 3 times.
"""count=1
while count <=3:
    print("Python is fun!")
    count+=1"""

# Infinite Loop + break (until user says stop)

while True:
    print("Python is fun!")
    userinput=input("Do you want to continue?(yes/no):")

    if userinput=="no":
        print("ok the loop stopped")
        break