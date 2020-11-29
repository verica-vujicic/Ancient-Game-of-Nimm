"""
File: ancient_game_of_nimm.py
- The game starts with a pile of 20 stones between the players
- The two players alternate turns
- On a given turn, a player may take either 1 or 2 stone from the center pile
- The two players continue until the center pile has run out of stones
- The last player to take a stone loses
"""

def main():

    print("Welcome to Ancient Game of Nimm!")
    game_on = True
    while game_on:
        stones_left = 20
        answer = ""
        player = 0
        while player != 1 and player != 2:
            player = int(input("Do you want to be Player 1 or Player 2? Please enter 1 or 2: "))
        print(f"Great! Player {player} will go first.")
        while stones_left != 0:
            stones_removed = 0
            if player == 1:
                while invalid_input(stones_removed):
                    stones_removed = int(input("Player 1, do you want to remove 1 or 2 stones? "))
                stones_left -= stones_removed
                player = 2
            else:
                while invalid_input(stones_removed):
                    stones_removed = int(input("Player 2, do you want to remove 1 or 2 stones? "))
                stones_left -= stones_removed
                player = 1
            print(f"There are {stones_left} stones left.")
        print(f"Congratulations, Player {player}! You have won!")
        while answer != "yes" and answer != "no":
            answer = (input("Wanna play again? Please enter Yes or No ")).lower()
        if answer == "no":
            game_on = False
            print("Goodbye!")

def invalid_input(x):
    return x != 1 and x != 2

if __name__ == '__main__':
    main()
