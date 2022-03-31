import random

# Just to play 😜!!

print("------------------------  GARGI'S NUMBER GUESSING GAME 🔢 !!! -----------------------")

name = input("Enter your name : ")

print( " Hello " + name + " !! , " + " Welcome to Gargi's Number Guessing Game")

number = random.randint(1,9)

chances = 0

guess = input("Enter the number, you guess : ") 

while chances < 5 :
    if int(guess)<number  :
        print("Your guess is too low , Guess a number higher than ", guess )
        guess = input("Enter the number, you guess : ") 
        chances = chances + 1
        
    elif int(guess)>number:
         print("Your guess is too high , Guess a number lesser than ", guess )
         guess = input("Enter the number, you guess : ") 
         chances = chances + 1

    else:
        print("Congratulations !! , You Won !!")
        break


if  not  chances < 5 :
    print("You Lose , The number is ", number)

