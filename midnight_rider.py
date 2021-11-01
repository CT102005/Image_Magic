# Midnight Rider

# A text based game of intrigue and illusion

import random
import sys
import textwrap
import time
import midnight_rider_text

# CONSTANTS
MAX_FUEL = 50
MAX_TOFU = 3

class Game:
    """Represent our game engine
    Attributes:
        done: describes if game is finished or not - bool
        distance travelled: describe the distance that we've travelled so far in this game in km
        amount of tofu: how much tofu we have left in our inventory
        agents_distance: describes the distance between the player and the agents
        fuel: Describes the amount of fuel remaining
    """
    def __init__(self):
        self.done = False
        self.distance_travelled = 0
        self.amount_tofu = 3
        self.agents_distance = -20
        self.fuel = MAX_FUEL

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text:str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()
        # Based on their choice, change the attributes of the class
        if user_choice == "d":
            self.fuel = MAX_FUEL

            # Decide how far the agents go
            self.agents_distance += random.randrange(7, 15)

            # Give the user feedback
            print(midnight_rider_text.REFUEL)
        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Travelled: {self.distance_travelled} km")
            print(f"Tofu pieces left: {self.amount_tofu}")
            print(f"Agent's Distance: {abs(self.agents_distance)} km behind")
            print(f"Fuel Left: {self.fuel}L")
            print("------------------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True

def main() -> None:
    game = Game() # Starting a new game
    game.introduction()

    # Main Loop:
    while not game.done:
        game.show_choices()
        game.get_choice()

if __name__ == "__main__":
    main()