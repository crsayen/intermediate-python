class Message:
    verb = "says"

    def __init__(self, author, content):
        self.author = author
        self.content = content

    def __str__(self):
        return f"{self.author} {self.__class__.verb} {self.content}"


class WhisperedMessage(Message):
    verb = "whispers"


myMessage = Message("Chris", "I've got a message")
myWhisperedMessage = WhisperedMessage("Chris", "I've got a secret")

print(myMessage)           # Chris says I've got a message
print(myWhisperedMessage)  # Chris whispers I've got a secret
