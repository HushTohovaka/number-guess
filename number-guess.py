# Import the random module
import random

# When to use break and continue
# Continue doesnt mean continue it means go back to the beginning
# Break means, break out of the inner most loop. Break is only used in for or while loops
# n = 5

# while n > 0:
#     n = n -1 
#     if n == 2:
#         break
#     print(n)
# print("Loop completed")

# n = 5
# while n > 0:
#     n = n -1 
#     if n == 2:
#         continue
#     print(n)
# print("Loop completed")



top_of_range = input("Type a number ")

# Check if the number they input is a digit , This will return True or False
if top_of_range.isdigit():
    # Change the type from a string to an integer
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number which is above 0")
        quit()
    # No need for an else statement here

else:
    print("Enter a number next time")
    quit()

# Random number generator
random_number = random.randint(0,top_of_range)
guesses = 0

# Using break and continue
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time ")
        continue
    
    if user_guess == random_number:
        # print("You got it in " + str(guesses) )
        break
    else:
        print("You got it wrong!")

        if user_guess > random_number:
            print("The number is lower")
        else:
            print("The number is higher")

print("You got it in", guesses, "guesses")


