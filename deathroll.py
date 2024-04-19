import random

def main():
    print("Welcome to deathrolling!")
    print("Here the players roll a six-sided dice, and whoever draws a 1, loses.")
    deathroll()

def deathroll():
    while True:
        player_1_roll = int(input("Player 1, please insert a number:\n"))
        roll1 = random.randint(1, player_1_roll)
        print(f"Player 1 rolls: {roll1}")

        if roll1 == 1:
            print("Player 1 loses!")
            break

        player_2_roll = int(input("Player 2, please insert a number:\n"))
        roll2 = random.randint(1, player_2_roll)
        print(f"Player 2 rolls: {roll2}")
        if roll2 == 1:
            print("Player 2 loses!")
            break

if __name__ == "__main__":
    main()
