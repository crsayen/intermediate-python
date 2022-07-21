class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content


myMessage = Message("Chris", "myMessage is an instance of the Message class")
print(myMessage.author)  # Chris
print(myMessage.content)  # myMessage is an instance of the Message class
