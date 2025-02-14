from brain_games.games import brain_prime
from brain_games.games_core import run_game


def main():
    run_game(brain_prime.DESCRIPTION, brain_prime.make_game_data)