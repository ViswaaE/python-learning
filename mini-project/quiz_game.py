print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0 


answer =input("What does CPU stands for? ")
if answer.lower() =="central processing unit":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What is the brain of the computer? ")
if answer.lower() == "cpu":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What type of device is a keyboard? ")
if answer.lower() == "input device":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("Which part of the computer stores data permanently? ")
if answer.lower() == "hard disk" or answer.lower() == "hard drive":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

answer = input("Which device is used to display output on screen? ")
if answer.lower() == "monitor":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")


print("You got "+str(score)+" question correct!")
print("You got "+str((score/10) *100)+"%")
