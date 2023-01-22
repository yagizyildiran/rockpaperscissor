import random

rpcList = ["Rock", "Paper", "Scissor"]

aiAnswer = random.choice(rpcList)

userAnswer = input("Rock Paper Scissor? ")


if userAnswer == "Rock" and aiAnswer == "Rock":
    print("Equal")
if userAnswer == "Rock" and aiAnswer == "Scissor":
    print("You won!")
if userAnswer == "Rock" and aiAnswer == "Paper":
    print("You lost!")
if userAnswer == "Paper" and aiAnswer == "Paper":
    print("Equal")
if userAnswer == "Paper" and aiAnswer == "Rock":
    print("You won!")
if userAnswer == "Paper" and aiAnswer == "Scissor":
    print("You lost!")
if userAnswer == "Scissor" and aiAnswer == "Scissor":
    print("Equal")
if userAnswer == "Scissor" and aiAnswer == "Paper":
    print("You won!")
if userAnswer == "Scissor" and aiAnswer == "Rock":
    print("You lost!")
if userAnswer != rpcList:
    print("Please input a defined variable")