class User:
    def __init__(self, name, __password, number, age, email):
        self.name = name
        self.__password = __password
        self.number = number
        self.age = age
        self.email = email

    def exception(self, name):

        for character in name:
            if character in "_.-{}[]":
                print(f"Characters not accepted in: {self.name}.")
                return
        else:
            print(f"Name: {self.name} approved")


class Post:
    def __init__(self, text, date, images, likes):
        self.text = text
        self.date = date
        self.images = images
        self.likes = likes

    def badWords(self,text):

        badWords = ["stupid", "idiot", "dumb", "bitch", "dylan", "kill yourself >:V"]

        if text in badWords:
            print(f"Your message {self.text} is not valid")
        else:
            print("Send message :)")



class Comments:
    def __init__(self, text, date, likes):
        self.text = text
        self.date = date
        self.likes = likes

    def badWords(self,text):

        badWords = ["stupid", "idiot", "dumb", "bitch", "dylan", "kill yourself >:V"]

        if text in badWords:
            print(f"Your message {self.text} is not valid")
        else:
            print("Send message :)")
            


class Message:
    def __init__(self, text, link, images, date, stickers):
        self.text = text
        self.link = link
        self.images = images
        self.date = date
        self.stickers = stickers

    def limit(self,text):
        if len(text) >=1000:
            print("Excess of characters in the box")
        else:
            print("Message accepted")

    def badWords(self,text):
    
            badWords = ["stupid", "idiot", "dumb", "bitch", "dylan", "kill yourself >:V"]

            if text in badWords:
                print(f"Your message {self.text} is not valid")
            else:
                print("Send message :)")

