#!/usr/bin/env python3

from MiniMaxOpening import MiniMaxOpening
from MiniMaxGame import MiniMaxGame
from MiniMaxOpeningBlack import MiniMaxOpeningBlack
from MiniMaxGameBlack import MiniMaxGameBlack
from ABOpening import ABOpening
from ABGame import ABGame
from MiniMaxOpeningImproved import MiniMaxOpeningImproved
from MiniMaxGameImproved import MiniMaxGameImproved


def mini_max_opening_main(input_file, output_file, depth):
    opening = MiniMaxOpening()
    opening.main(input_file, output_file, depth)


def mini_max_game_main(input_file, output_file, depth):
    game = MiniMaxGame()
    game.main(input_file, output_file, depth)


def ab_opening_main(input_file, output_file, depth):
    opening = ABOpening()
    opening.main(input_file, output_file, depth)


def ab_game_main(input_file, output_file, depth):
    game = ABGame()
    game.main(input_file, output_file, depth)


def mini_max_opening_black_main(input_file, output_file, depth):
    opening = MiniMaxOpeningBlack()
    opening.main(input_file, output_file, depth)


def mini_max_game_black_main(input_file, output_file, depth):
    game = MiniMaxGameBlack()
    game.main(input_file, output_file, depth)


def mini_max_opening_improved_main(input_file, output_file, depth):
    opening = MiniMaxOpeningImproved()
    opening.main(input_file, output_file, depth)


def mini_max_game_improved_main(input_file, output_file, depth):
    game = MiniMaxGameImproved()
    game.main(input_file, output_file, depth)


if __name__ == "__main__":
    while True:
        command = input(">>> ")
        parts = command.split()

        if command.lower() in ["exit", "quit"]:
            break

        if len(parts) == 4:
            input_file, output_file, depth = parts[1], parts[2], int(parts[3])

            if parts[0] == "MiniMaxOpening":
                mini_max_opening_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxGame":
                mini_max_game_main(input_file, output_file, depth)
            elif parts[0] == "ABOpening":
                ab_opening_main(input_file, output_file, depth)
            elif parts[0] == "ABGame":
                ab_game_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxOpeningBlack":
                mini_max_opening_black_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxGameBlack":
                mini_max_game_black_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxOpeningImproved":
                mini_max_opening_improved_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxGameImproved":
                mini_max_game_improved_main(input_file, output_file, depth)
            else:
                print("Invalid command. Please use the correct format.")
        else:
            print("Invalid command. Please use the correct format.")
