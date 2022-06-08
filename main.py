#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def game_rps():
    win_r, win_h = 0, 0
    n = 1
    while n <= 3:
        user_input = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        random.shuffle(possible_actions)
        robot_input = random.choice(possible_actions)
        print(f"\nYou chose {user_input}, computer chose {robot_input}.\n")

        if user_input == robot_input:
            print(f"Both players selected {user_input}. It's a tie!\n")
            n+=1
            win_r += 1
            win_h += 1
        elif user_input == "rock":
            if robot_input == "scissors":
                print("You win!\n")
                win_h += 1
                
            else:
                print("You lose\n")
                win_r += 1
            n+=1       
        elif user_input == "paper":
            if robot_input == "rock":
                print("You win!\n")
                win_h += 1
                
            else:
                print("You lose\n")
                win_r += 1
            n+=1       
        elif user_input == "scissors":
            if robot_input == "paper":
                print("You win!\n")
                win_h += 1
                
            else:
                print("You lose\n")
                win_r += 1
            n+=1
    if win_r < win_h:
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\nYou won the game")
    elif win_h == win_r:
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\nThe game equalised")
    else:
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\nComputer won the game")
game_rps()

