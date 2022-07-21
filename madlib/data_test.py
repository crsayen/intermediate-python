from .data import Data


def test_get_random_word():
    data = Data()
    assert data.get_random_word("noun") in data.words["noun"]
    assert data.get_random_word("adjective") in data.words["adjective"]
    assert data.get_random_word("place") in data.words["place"]
    assert data.get_random_word("person") in data.words["person"]
    assert data.get_random_word("plural") in data.words["plural"]


def test_get_random_story():
    data = Data()
    assert data.get_random_story() in data.stories
