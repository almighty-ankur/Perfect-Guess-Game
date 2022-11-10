
import random

player1 = input("Player 1 - Enter Your Name : \n")
player2 = input("Player 2 - Enter Your Name : \n")

starting1 = int(input("Enter The Starting Number :\n"))
ending1 = int(input("Enter The Ending Number :\n"))

c = random.randint(starting1,ending1)


try1 = 1

n = int(input(f"Enter Your Guess {player1} between {starting1} to {ending1} :\n"))

while n!=c:
	if n>c:
		n = int(input(f"{player1} Wrong Guess Enter A Smaller number!  :\n"))
		try1 = try1+1
	else:
		n = int(input(f"{player1} Wrong Guess Enter A Bigger Number!  :\n"))
		try1 = try1+1

print(f"Number Guessed! You Took {try1} Tries!")


print(f"\n{player2}'s Turn To Guess The Number! \nHave Fun :)")

try2 = 1


e = random.randint(starting1,ending1)


n = int(input(f"Enter Your Guess {player2} between {starting1} to {ending1} :\n"))

while n!=e:
	if n>e:
		n = int(input(f"Wrong Guess Enter A Smaller number! {player2} :\n"))
		try2 = try2+1
	else:
		n = int(input(f"Wrong Guess Enter A Bigger Number! {player2} :\n"))
		try2 = try2+1

print(f"Number Guessed! You Took {try2} Tries!\n")

if try1>try2:
	print(f"{player2} Won!")
elif(try2>try1):
	print(f"{player1} Won!")
else:
	print("It's a Draw!")
