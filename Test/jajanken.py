import random

user_w = 0
comp_w = 0

options = ["r", "p", "s", "q"]

while True:
    user_input = input ("Type rock-R/ paper - P/ scissors -S or Q to quit:  ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    random_no = random.randint(0, 2)
    comp_pick = options[random_no]
    
    print("Computer picked", comp_pick + ".")

    if user_input == "r" and comp_pick=="s":
        print("You won!")
        user_w += 1

    elif user_input == "p" and comp_pick=="r":
         print("You won!")
         user_w += 1

    elif user_input == "s" and comp_pick=="p":
        print("You won!")
        user_w += 1
    elif user_input == comp_pick:
        print("You drew")
        user_w += 1
        comp_w +=1
    
    else:
        print("You lost that round")
        comp_w +=1

print("You won", user_w,"times")
print("The computer won",comp_w,"times")

print("Goodbye!")
input()
