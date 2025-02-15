from brain_games.games import brain_gcd
from brain_games.games_core import run_game


def main():
    run_game(brain_gcd.DESCRIPTION, brain_gcd.make_game_data)