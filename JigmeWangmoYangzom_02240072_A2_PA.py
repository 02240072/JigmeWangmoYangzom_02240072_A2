def game_menu():
    print("Welcome to Game World")
    print("1. guess the number")
    print("2. Rock Paper Scissor")
    print("3. Trivia Persuit Game")
    print("4. Pokemon card binder")
    print("5. Exit")
    game_choice= int(input("Select game:"))          
    return game_choice
game_choice = game_menu()

import random
class GuessNumberGame:
    def __init__(self):
        self.max_attempts = 5
        self.upper_limit = 100
        self.lower_limit = 1
        self.number_to_guess = random.randint(self.lower_limit, self.upper_limit)

    def play_game(self):
        for attempt in range(1, self.max_attempts + 1):                                    # to include the max attempt which is 5, self.max_attempts + 1 is used inorder to let the user to guess the number 5 times
            user_choice = int(input("Enter a number:"))
            if user_choice < self.lower_limit or user_choice > self.upper_limit:
                print("Invalid input. Please enter a number between 1 and 100.")
            if user_choice == self.number_to_guess:
                print(f"Congratulations! You've guessed the number {self.number_to_guess} in {attempt} attempts.")
                break
            elif user_choice < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high!")

        else:
            print(f"Sorry, you've used all your attempts. The number was {self.number_to_guess}.")


class RockPaperScissors:
    def __init__(self,computer_score = 0, user_score = 0):
        self.choices_available = ["rock", "paper", "scissor"]
        self.computer_score = computer_score
        self.user_score = user_score 

    def play_game(self):
        for round in range(1, 6):
            self.computer_choice = random.choice(self.choices_available)
            user_choice = input("Your choice(rock or paper or scissor):") 
            print("The Computer's choice:", self.computer_choice)  
            if user_choice == self.computer_choice or user_choice == self.computer_choice:
                print("Draw")
            elif (user_choice == "rock" and self.computer_choice == "paper") or (user_choice == "scissor" and self.computer_choice == "rock") or (user_choice == "paper" and self.computer_choice == "scissor"):
                print(f"You lose this round {round}")
                self.computer_score += 1
            else:
                print(f"you won! this round {round}")
                self.user_score += 1
        while True:
            print(f"user_score: {self.user_score} ")
            print(f"computer_score: {self.computer_score}")
            if self.user_score == self.computer_score:
                print ("Draw")
            elif self.user_score > self.computer_score:
                print ("You won! :) ")
            else:
                print ("You lose! ;( ")
            break


class Trivia_Question_Game:
    def __init__(self, math):
        self.score = 0
        self.math = math

    def play_game(self):    
        self.choice = input("Choose a category (math, GK): ")
        
        if self.choice == "math":
            print("What is 2 + 2?")
            print("options: [a.2, b.3, c.4]")
            self.answer = "c"
            user_answer = input("Your answer(a/b/c): ")
            if user_answer == self.answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

            print("What is the square root of -1?")
            print("options: [a.1, b.i, c.-1]")
            self.answer = "b"
            user_answer = input("Your answer(a/b/c): ")
            if user_answer == self.answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

        else:
            print("What is the capital of Bhutan")
            print("options: [a.Thimphu, b.Wangdue, c.Paro]")
            self.answer = "a"
            user_answer = input("Your answer(a/b/c): ")
            if user_answer == self.answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

            print("What is the largest dessert in the world?")
            print("options: [a.Sahara, b.Gobi, c.Antarctica,]")
            self.answer = "c"
            user_answer = input("Your answer(a/b/c): ")
            if user_answer == self.answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        print(f"Your score is {self.score}.")


def Exit():
    u = input("Do yo really want to EXIT(yes or no):")
    if u == "no":
        game_menu()                 
    else:
        print("Thank you for playing!")

while True:
    if game_choice == 5:
         Exit()                    
         break                      
    elif game_choice == 1:
        GuessNumberGame = GuessNumberGame()
        GuessNumberGame.play_game()            
    elif game_choice == 2:          
        RockPaperScissors = RockPaperScissors()
        RockPaperScissors.play_game() 
    elif game_choice == 3:
        game = Trivia_Question_Game("math")
        game = Trivia_Question_Game("general_knowledge")
        game.play_game() 
    else:
       import JigmeWangmoYangzom_02240072_A2_PB  

    z = input("do you want to play again (yes or no):")
    if z.lower() == "no":
        Exit()
        break 
    else:                      
        game_choice = game_menu()




