print('Welcome to my computer quiz')

playing = input("Do you wanna play? ")
print(playing)

if playing != "yes":
    quit()
print("Okay! Let's Play")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does ALU stand for? ").lower()
if answer == "arithmetic logic unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
    
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str(score /3 * 100 ) + "%")
