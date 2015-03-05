import random
RANKS =["A", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]

Player1Counter=0
Player2Counter=0
print("Welcome to WAR!")
print("You and a friend will player war until one of the two of you get ten points!")
print("Before we begin, Can you please enter our names.")
Player1Name=input("Player 1 Name: ")
Player2Name=input("Player 2 Name: ")
while Player1Counter < 10 and Player2Counter < 10:
  Player1CardIndex=random.randrange(len(RANKS))
  Player2CardIndex=random.randrange(len(RANKS))
  Player1Card=RANKS[Player1CardIndex]
  Player2Card=RANKS[Player2CardIndex]
  if Player1CardIndex > 8:
    Player1CardIndex = 10
  if Player2CardIndex > 8:
    Player2CardIndex = 10
  Player1Suit=random.choice(SUITS)
  Player2Suit=random.choice(SUITS)
  Player1Card =Player1Card + Player1Suit
  Player2Card = Player2Card + Player2Suit
  print(Player1Name,":",Player1Card)
  print(Player2Name,":",Player2Card)
  if Player1CardIndex > Player2CardIndex:
    print(Player1Name,"has won this round and has gained one point.")
    Player1Counter += 1
  elif Player1CardIndex < Player2CardIndex:
    print(Player2Name,"has won this round and has gained one point.")
    Player2Counter += 1
  else:
    print("Oh No! No one has won this round1")
  print(Player1Name,":",Player1Counter)
  print(Player2Name,":",Player2Counter)
  input("Please press the <Enter> key.")
if Player1Counter < Player2Counter:
  print(Player1Name,"has won and is the ultimate champion!")
else:
  print(Player2Name,"has won and is the ulimate champion!")
print("Thanks for playing.")
input("Please press <Enter> to exit.")
  
