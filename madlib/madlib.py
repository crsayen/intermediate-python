from functools import lru_cache


class InvalidTokenError(Exception):
    "raised when an invalid template is passed"
    pass


class Madlib:
    prompts = ["noun",
               "plural",
               "adjective",
               "place",
               "person"]

    def __init__(self, madlib_text):
        self.madlib_text = madlib_text
        self.prompts = Madlib.extract_prompts(madlib_text)
        self.prompt_iterator = iter(self.prompts)
        self.answers = []

    def get_next_prompt(self):
        try:
            return next(self.prompt_iterator)
        except StopIteration:
            return None

    def give_next_answer(self, answer):
        self.answers.append(answer)

    def solve(self):
        formatable_text = self.madlib_text
        for prompt in self.prompts:
            formatable_text = formatable_text.replace(prompt, "")
        return formatable_text.format(*self.answers)

    @staticmethod
    def is_prompt_token(word):
        if (isPromptToken := word.startswith("{")) != word.endswith("}"):
            raise InvalidTokenError
        return isPromptToken

    @staticmethod
    def remove_punctuation(text):
        punctuation_chars = [".", ",", "!", "?", ";", ":", "'", '"']
        return "".join([o for o in text if not o in punctuation_chars])

    @staticmethod
    def remove_brackets(word):
        return word.replace("{", "").replace("}", "")

    @staticmethod
    def extract_prompts(text):
        text_no_punctuation = Madlib.remove_punctuation(text)
        text_words = text_no_punctuation.split(" ")
        words_to_fill = [
            Madlib.remove_brackets(word)
            for word in text_words
            if Madlib.is_prompt_token(word)
        ]
        if [word for word in words_to_fill if word not in Madlib.prompts]:
            raise InvalidTokenError
        return words_to_fill
