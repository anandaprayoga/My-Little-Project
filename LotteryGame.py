import random

# Generate a lottery number
lottery = random.randint(100, 999)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery % 100

# Get digits from guess
guessDigit1 = guess // 100
guessDigit2 = guess % 100

print("The lottery number is", lottery)

# Check the guess 20
if guess == lottery:
	print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
	print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
	print("Match one digit: you win $1,000")
else:
	print("Sorry, no match")
