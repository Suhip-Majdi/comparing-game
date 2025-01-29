# # from art_data_Instgrame import *
# # import random
# #
# #
# # def rand_person():
# #     return random.choice(data)
# #
# #
# #
# # def game():
# #     print(logo)
# #
# #     score=0
# #
# #     person_1=rand_person()
# #     person_2=rand_person()
# #
# #     game_countine=True
# #
# #     while game_countine:
# #
# #         while person_1==person_2:
# #             person_2=rand_person()
# #
# #         person_1 = rand_person()
# #         person_2 = rand_person()
# #
# #         print(f"comper A ,{person_1['name']} , {person_1['description']} , from {person_1['country']} LLLLLLLLLLL{person_1['follower_count']}")
# #         print(vs)
# #
# #         print(f"Aginst B : {person_2['name']} , {person_2['description']} , from {person_2['country']}llllllllll{person_2['follower_countB'
# #                                                                                                                           '']}")
# #
# #         gusse=input("How has more followers ? type A or B : ")
# #
# #         if person_1['follower_count']>person_2['follower_count'] and gusse=='A':
# #            score+=1
# #            print(f"you are right! curront scor is {score}")
# #
# #         elif person_2['follower_count']>person_1['follower_count'] and gusse =='B':
# #             score+=1
# #             print(f"you are right! curront scor is {score}")
# #
# #         else:
# #             game_countine=False
# #             print(f"sorry that's wrong , your finall scor {score} ")
# #
# # game()
#

from compering_game.art_data_Instgrame import *
import random

def rand_person():
    return random.choice(data)

def format(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(person_1,person_2,gusse):
    if person_1>person_2:
        return gusse=='A'
    else:
        return gusse=='B'

#TODO :2;KJAGOMPQM

def game():
    print(logo)
    scor=0

    person_1=rand_person()
    person_2=rand_person()

    game_countine=True

    while game_countine:

        while person_1 == person_2:
            person_2 = rand_person()

        person_1 = rand_person()
        person_2 = rand_person()

        print(f"comper A ,{person_1['name']} , {person_1['description']} , from {person_1['country']} LLLLLLLLLLL{person_1['follower_count']}")
        print(vs)

        print(f"Aginst B : {person_2['name']} , {person_2['description']} , from {person_2['country']}llllllllll{person_2['follower_count']}")

        gusse=input("How has more followers ? type A or B : ")

        a_follower=person_1['follower_count']
        b_follower=person_2['follower_count']

        is_correct=check_answer(a_follower,b_follower,gusse)

        if is_correct:
            scor += 1
            print(f"You're right! Current score: {scor}.")
        else:
            game_countine = False
            print(f"Sorry, that's wrong. Final score: {scor}")

game()

# #
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear
#
#
# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
#
# def formatt(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
# #TODO :2;KJAGOMPQM
# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {formatt(account_a)}.")
#         print(vs)
#         print(f"Against B: {formatt(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         clear()
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()
#
# '''
#
# FAQ: Why does choice B always become choice A in every round, even when A had more followers?
#
# Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)
#
# '''
#
# # Generate a random account from the game data.
#
# # Format account data into printable format.
#
# # Ask user for a guess.
#
# # Check if user is correct.
# ## Get follower count.
# ## If Statement
#
# # Feedback.
#
# # Score Keeping.
#
# # Make game repeatable.
#
# # Make B become the next A.
#
# # Add art.
#
# # Clear screen between rounds.