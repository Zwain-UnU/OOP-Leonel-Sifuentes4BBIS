class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, title, author):
        self.title = title
        self.author = author

user1 = User("Carlos")
post1 = Post("My first post", user1)

print(post1.author.name)



