import unittest
from s22 import Message

expectedAuthor = "author"
expectedContent = "content"


class TestMessageClass(unittest.TestCase):
    def test_message_constructor(self):
        message = Message(expectedAuthor, expectedContent)
        self.assertEqual(message.author, expectedAuthor)
        self.assertEqual(message.content, expectedContent)

    def test_message_str(self):
        message = Message(expectedAuthor, expectedContent)
        message_string = f"{message}"
        self.assertEqual(
            message_string, f"{expectedAuthor} says {expectedContent}")
