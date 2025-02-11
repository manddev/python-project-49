from brain_games.games_core import make_game
from brain_games.games.brain_progression import make_game_data, DESCRIPTION


def main():
    make_game(DESCRIPTION, make_game_data)