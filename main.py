#!/usr/bin/env python3

import sys
import os

# Determine if running as a script or as a compiled file
if __file__.endswith('.pyc'):
    # If running as compiled file in bin, adjust path accordingly
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
else:
    # If running as a script, use the original path setup
    sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from typing import Callable, Any
from utils.util import (
    get_positions_evaluated,
    reset_positions_evaluated,
    open_board,
    write_best_move,
    display_help,
    ascii_title,
    print_board,
    get_ascii_board_path
)
from modules.minimax_opening import MiniMaxOpening
from modules.minimax_game import MiniMaxGame
from modules.ab_opening import ABOpening
from modules.ab_game import ABGame
from modules.minimax_opening_black import MiniMaxOpeningBlack
from modules.minimax_game_black import MiniMaxGameBlack
from modules.minimax_opening_improved import MiniMaxOpeningImproved
from modules.minimax_game_improved import MiniMaxGameImproved
from modules.ab_opening_improved import ABOpeningImproved
from modules.ab_game_improved import ABGameImproved


# Dictionary to map commands to game classes
command_mapping = {
    "MiniMaxOpening": MiniMaxOpening,
    "MiniMaxGame": MiniMaxGame,
    "ABOpening": ABOpening,
    "ABGame": ABGame,
    "MiniMaxOpeningBlack": MiniMaxOpeningBlack,
    "MiniMaxGameBlack": MiniMaxGameBlack,
    "MiniMaxOpeningImproved": MiniMaxOpeningImproved,
    "MiniMaxGameImproved": MiniMaxGameImproved,
    "ABOpeningImproved": ABOpeningImproved,
    "ABGameImproved": ABGameImproved
}


# Dictionary to map game classes to messages
class_name_to_message = {
    "ABOpening": "Alpha-Beta Pruning estimate: {}.",
    "ABGame": "Alpha-Beta Pruning estimate: {}.",
    "ABOpeningImproved": "Improved Alpha-Beta Pruning estimate: {}.",
    "ABGameImproved": "Improved Alpha-Beta Pruning estimate: {}.",
    "MiniMaxOpeningImproved": "Improved MINIMAX estimate: {}.",
    "MiniMaxGameImproved": "Improved MINIMAX estimate: {}.",
    "MiniMaxOpeningBlack": "MINIMAX estimate for black: {}.",
    "MiniMaxGameBlack": "MINIMAX estimate for black: {}."
}


def game_main(game_class: Callable[..., Any], input_file: str, output_file: str, depth: int):
    """
    Executes the main game logic using the specified game class.

    This function initializes the game, reads the board state from an input file,
    computes the best move using the game's play_game method, and writes the best move to an output file.
    It also prints the input and output positions, the number of positions evaluated,
    and the static estimation for the game's outcome.

    Parameters:
    - game_class (Callable[..., Any]): The class of the game to be played.
      This class should have a play_game method.
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the game's search algorithm.

    Exceptions:
    - Catches and prints any exceptions that occur during the game's execution.

    Returns:
    - None
    """
    try:
        game = game_class()
        board = open_board(input_file)
        ascii_board = get_ascii_board_path()
        estimate, best_move = game.play_game(board, depth)

        write_best_move(output_file, best_move)

        # Get the ASCII board representations
        initial_board_str = print_board(input_file, ascii_board)
        new_board_str = print_board(output_file, ascii_board)

        # Split the board strings into lines for side-by-side printing
        initial_board_lines = initial_board_str.split('\n')
        new_board_lines = new_board_str.split('\n')

        # Print the boards side by side with consistent spacing
        print("\nInput Board State: " + " " * 22 + "Output Board State:\n")
        for initial_line, new_line in zip(initial_board_lines, new_board_lines):
            print(f"{initial_line:40} {new_line}")

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")

        # Depending on the class the estimate is printed differently
        class_name = game.__class__.__name__
        message = class_name_to_message.get(class_name, "MINIMAX estimate: {}.")
        print(message.format(estimate))

    except Exception as e:
        print(f"\nError: {e}")


def main():
    ascii_title()
    print("Instructions: \n")
    print("\t1. Enter the command followed by the input file, output file, and depth.")
    print("\t2. Input files must be in the provided test_files directory.\n")
    print("Format: \n")
    print("\t<command> <input_file.txt> <output_file.txt> <depth>\n")
    print("Example input: \n")
    print("\tMiniMaxOpening board1.txt board2.txt 2\n")
    print("Type 'help' for a list of acceptable commands.")
    print("Type 'exit' or 'quit' to end the program.")

    while True:
        try:
            command = input("\nEnter input >>> ")
            parts = command.split()

            if command.lower() in ["exit", "quit"]:
                break
            elif command.lower() == "help":
                display_help()
                continue

            if len(parts) == 4:
                input_file, output_file = parts[1], parts[2]
                try:
                    depth = int(parts[3])
                except ValueError:
                    print("\nError: Depth must be an integer.")
                    continue

                if parts[0] in command_mapping:
                    reset_positions_evaluated()
                    game_main(command_mapping[parts[0]], input_file, output_file, depth)
                else:
                    raise Exception("Invalid command. Please use the correct format.")
            else:
                raise Exception("Invalid command. Please use the correct format.")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
