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
MAX_HUNGER = 50
MAX_DISTANCE = 100
ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL": 2,
    "LOSE_HUNGER": 3,
    "WIN": 4
}


class Game:
    """Represent our game engine
    Attributes:
        done: describes if game is finished or not - bool
        distance travelled: describe the distance that
            we've travelled so far in this game in km
        amount of tofu: how much tofu we have left in our inventory
        agents_distance: describes the distance between the player and the agents
        fuel: Describes the amount of fuel remaining
        hunger: describes how hungry the player is,
            represented by a number between 0-50,
            if hunger goes beyond 50, game is over
        endgame_reason: shows the index of the game
            ending text from midnight_rider_text,py
    """
    def __init__(self):
        self.done = False
        self.distance_travelled = 0
        self.amount_tofu = 3
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = -1

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.01)
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
        agents_distance_now = random.randrange(7, 15)
        if user_choice == "a":
            if self.amount_tofu > 0:
                self.amount_tofu -= 1
                self.hunger = 0
                print(midnight_rider_text.EAT_TOFU)
            else:
                # Tell the player they have no tofu
                print(midnight_rider_text.NO_TOFU)
        elif user_choice == "b":
            player_distance_now = random.randrange(3, 8)
            self.distance_travelled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn fuel
            self.fuel -= random.randrange(2, 7)
            # Give the player some feedback
            print(f"\n--------You drive conservatively.")
            print(f"---------You travelled {player_distance_now} km")
        elif user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_travelled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn fuel
            self.fuel -= random.randrange(5, 11)
            # Give the player some feedback
            print(f"\n--------ZOOOOOOOOOOOOOOOM.")
            print(f"---------You travelled {player_distance_now} km")
        elif user_choice == "d":
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
        if user_choice in ["b", "c", "d"]:
            self.hunger += random.randrange(8, 18)

    def upkeep(self) -> None:
        # Give the user reminders of hunger
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

            time.sleep(1)

    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met, change the self.done flag."""
        # TODO: LOSE - Agents catch up to the player
        if self.agents_distance >= 0:
            # Allows us to quit the while loop
            self.done = True
            # Helps with printing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]  # TODO
        # TODO: LOSE - Fuel runs out
        if self.fuel <= 0:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]

        # TODO: LOSE - Perish because of hunger
        if self.hunger > MAX_HUNGER:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]
        # TODO: WIN - reach the goal
        if self.distance_travelled >= MAX_DISTANCE:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["WIN"]


def main() -> None:
    game = Game()   # Starting a new game
    game.introduction()

    # Main game loop:
    while not game.done:
        game.upkeep()
        game.show_choices()
        game.get_choice()
        game.check_endgame()

    time.sleep(3)
    # Print out the ending
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )


if __name__ == "__main__":
    main()
