from brain_games.games import brain_gcd
from brain_games.games_core import make_game


def main():
    make_game(brain_gcd.DESCRIPTION, brain_gcd.make_game_data)