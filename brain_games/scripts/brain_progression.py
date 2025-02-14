from brain_games.games import brain_progression
from brain_games.games_core import run_game


def main():
    run_game(brain_progression.DESCRIPTION, brain_progression.make_game_data)