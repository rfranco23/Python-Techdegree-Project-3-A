import re

from phrasehunter.game import Game


if __name__ == '__main__':
    with open('phrases.txt') as phrase_file:
        data = phrase_file.read()
        list_of_phrases = re.findall(r"[\w?' ]+", data)
        
    game = Game(list_of_phrases)
    game.start_game()