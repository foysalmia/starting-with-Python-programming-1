player1 = input("Player 1 : ")
player2 = input("Player 2 : ")

if player1 == "rock" and player2 == "paper":
    print("Player 2 is the winner")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 is the winner")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 is the winner")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 is the winner")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 is the winner")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 is the winner")
else:
    print("The match is tied")
