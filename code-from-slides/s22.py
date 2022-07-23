class Message:
    verb = "says"

    def __init__(self, author, content):
        self.author = author
        self.content = content

    def __str__(self):
        return f"{self.author} {self.__class__.verb} {self.content}"


class WhisperedMessage(Message):
    verb = "whispers"


class ScreamedMessage(Message):
    verb = "screams"

    def scream_it(self):
        print(self.content.upper())


myMessage = Message("Chris", "I've got a message")
myWhisperedMessage = WhisperedMessage("Chris", "I've got a secret")
myScreamedMessage = ScreamedMessage("Chris", "I've got the power!")

print(myMessage)           # Chris says I've got a message
print(myWhisperedMessage)  # Chris whispers I've got a secret
myScreamedMessage.scream_it()  # I'VE GOT THE POWER!
