import json
import os
import random

DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "data")
WORDS_FILE = os.path.join(DATA_DIRECTORY, "words.json")
STORIES_DIRECTORY = os.path.join(DATA_DIRECTORY, "stories")


class Data:
    def __init__(self):
        self.stories = []

        with open(WORDS_FILE) as words_file:
            self.words = json.load(words_file)

        for filename in os.listdir(STORIES_DIRECTORY):
            f = os.path.join(STORIES_DIRECTORY, filename)
            if os.path.isfile(f):
                with open(f) as story_file:
                    self.stories.append(story_file.read())

    def get_random_word(self, typeof_word):
        return self.words[typeof_word][
            random.randint(0, len(self.words[typeof_word]) - 1)
        ]

    def get_random_story(self):
        return self.stories[random.randint(0, len(self.stories) - 1)]

