from .madlib import InvalidTokenError, Madlib
import unittest


class Madlib_test(unittest.TestCase):
    def test_is_template(self):
        assert Madlib.is_prompt_token("{noun}")
        assert not Madlib.is_prompt_token("noun")

    def test_remove_punctuation(self):
        assert Madlib.remove_punctuation("Hello, world!") == "Hello world"

    def test_remove_template_brackets(self):
        assert Madlib.remove_brackets("{noun}") == "noun"

    def test_extract_prompts(self):
        text = "find {noun}, {adjective}, and {place}. and {person}!"
        assert list(Madlib.extract_prompts(text)) == [
            "noun",
            "adjective",
            "place",
            "person",
        ]

    def test_get_prompt(self):
        madlib = Madlib("{noun}")
        assert madlib.get_next_prompt() == "noun"
        assert madlib.get_next_prompt() == None

    def test_prompt_iterator(self):
        madlib = Madlib("{adjective} {noun} in {place}! - {person}")
        count = 0
        for _ in madlib.prompt_iterator:
            count += 1
        assert count == 4

    def test_invalid_prompt_throws_exception(self):
        with self.assertRaises(InvalidTokenError):
            Madlib("{noun} in {badprompt}")
        with self.assertRaises(InvalidTokenError):
            Madlib("{} is empty")
        with self.assertRaises(InvalidTokenError):
            Madlib("{noun } has extra space")

    def test_madlib(self):
        madlib = Madlib("{adjective} {noun} in {place}! - {person}")
        assert madlib.get_next_prompt() == "adjective"
        madlib.give_next_answer("red")
        assert madlib.get_next_prompt() == "noun"
        madlib.give_next_answer("goose")
        assert madlib.get_next_prompt() == "place"
        madlib.give_next_answer("the mall")
        assert madlib.get_next_prompt() == "person"
        madlib.give_next_answer("Pythonista")
        assert madlib.solve() == "red goose in the mall! - Pythonista"
