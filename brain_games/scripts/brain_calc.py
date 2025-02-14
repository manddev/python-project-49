from brain_games.games import brain_calc
from brain_games.games_core import run_game


def main():
    make_game(brain_calc.DESCRIPTION, brain_calc.make_game_data)