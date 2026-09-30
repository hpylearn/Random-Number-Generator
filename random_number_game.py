import random
computer_choice = random.randint(1, 10)
user_choice = int(input("Enter your Choice: "))
print("computer choice is : ", computer_choice)
if computer_choice == user_choice:
    print("you Win")
else:
    print("You Lose")