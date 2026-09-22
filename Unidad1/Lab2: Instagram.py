class User:
    def __init__(self, name, __password, number, age, email):
        self.name = name
        self.__password = __password
        self.number = number
        self.age = age
        self.email = email
        self.mensajes = []

    def login(self):
        print("The user is logged")
    
    def create_post(self, text, date, images, likes):
        return Post(text, date, images, likes, autor=self)

    def comentar(self, texto, date, likes, post):
        nuevo_comentario = Comments(texto, date, likes, receiver=self)
        
        if not nuevo_comentario.badWords(texto):
            post.comentarios.append(nuevo_comentario)
            print(f"El usuario {self.name} comentó en el post de {post.autor.name}")

    def enviar_mensaje(self, receiver, text, link, images, date, stickers):
        nuevo_mensaje = Message(text, link, images, date, stickers, sender=self)
        
        nuevo_mensaje.limit(text)
        
        if not nuevo_mensaje.badWords(text):
            receiver.mensajes.append(nuevo_mensaje)
            print(f"Mensaje enviado de {self.name} a {receiver.name}")

    def exception(self, name):
        print("HOLA")
        for character in name:
            if character in "_.-{}[]":
                print(f"Characters not accepted in: {self.name}.")
                return
        else:
            print(f"Name: {self.name} approved")
   

class Post:
    def __init__(self, text, date, images, likes, autor):
        self.text = text
        self.date = date
        self.images = images
        self.likes = likes
        self.autor = autor
        self.comentarios = [] 

    def badWords(self, text):
        badWords = ["stupid", "idiot", "dumb", "bitch", "dylan", "kill yourself >:V"]
        for word in badWords:
            if word in text.lower():
                print(f"Your message '{text}' is not valid")
                return True
        print("Send message :)")
        return False

    def show(self):
        print(f"The user {self.autor.name} posted: {self.text}")


class Comments:
    def __init__(self, text, date, likes, receiver):
        self.text = text
        self.date = date
        self.likes = likes
        self.receiver = receiver

    def badWords(self, text):
        badWords = ["stupid", "idiot", "dumb", "bitch", "dylan", "kill yourself >:V"]
        for word in badWords:
            if word in text.lower():
                print(f"Your message '{text}' is not valid")
                return True
        print("Send message :)")
        return False
            

class Message:
    def __init__(self, text, link, images, date, stickers, sender):
        self.text = text
        self.link = link
        self.images = images
        self.date = date
        self.stickers = stickers
        self.sender = sender

    def limit(self, text):
        if len(text) >= 1000:
            print("Excess of characters in the box")
        else:
            print("Message accepted")

    def badWords(self, text):
        badWords = ["stupid", "idiot", "dumb", "bitch", "dylan", "kill yourself >:V"]
        for word in badWords:
            if word in text.lower():
                print(f"Your message '{text}' is not valid")
                return True
        print("Send message :)")
        return False


usuario1 = User("Juan", "123", "618", "19", "Leonel@gmail.com")
usuario2 = User("Omar", "1234", "6182590911", "20", "omar@utd.edu.mx")

posteo = usuario1.create_post("Hi everyone! I'm a IT Engineer", "2023-10-27", "foto.jpg", 0)
posteo.show()

usuario2.comentar("Muy bueno tu post", "2023-10-27", 0, posteo)

usuario1.enviar_mensaje(usuario2, "Hola Omar, gracias por el comentario", "youtube.com", "img.jpg", "2023-10-27", "sticker_feliz")

