class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content

    def toString(self):
        return f"{self.author} says {self.content}"


myMessage = Message("Chris", "Python will pass 'self' automatically")
print(myMessage.toString())
