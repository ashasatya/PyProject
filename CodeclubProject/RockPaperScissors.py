from random import randint

player = input('rock(O), paper(__), scissor(>)? ')
# player = input('rock(r), paper(p), scissor(s)? ')
print(player)
choosen = randint(1,3)
# print(choosen)
# if choosen == 1:
#     computer = 'r'
# elif choosen == 2:
#     computer = 'p'
# else:
#     computer = 's'
# print(computer)
# if player == computer:
#     print("DRAW")
# elif player == 'r' and computer == 's':
#     print("Player Wins")
# elif player == 's' and computer == 'p':
#     print("Player Wins")
# elif player == 'p' and computer == 'r':
#     print("Player Wins")
# else:
#     print("Computer WINS")

if choosen == 1:
    computer = 'O'
elif choosen == 2:
    computer = '__'
else:
    computer = '>'
print(computer)
if player == 'O' and computer == '>':
    print("Player Wins")
elif player == '>' and computer == '__':
    print("Player Wins")
elif player == "__" and computer == 'O':
    print("Player Wins")
elif player == computer:
    print("DRAW")
else:
    print("Computer WINS")