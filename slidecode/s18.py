class Message:
    verb = "says"

    def __init__(self, author, content):
        self.author = author
        self.content = content

    def __str__(self):
        return f"{self.author} {self.__class__.verb} {self.content}"


myMessage = Message("Chris", "Every object has a __class__ property")
print(myMessage)
