from brain_games.games import brain_even
from brain_games.games_core import run_game


def main():
    run_game(brain_even.DESCRIPTION, brain_even.make_game_data)