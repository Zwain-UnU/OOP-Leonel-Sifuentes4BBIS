from tkinter import Tk

from Views.login_view import LoginView
from Models.user_model import UserModel
from Models.autenticacion import Authentication

class System:
    def __init__(self):
        self.root = Tk()

    def start(self):
        vista = LoginView(self.root)
        modelo = UserModel()
        Authentication(modelo, vista)

        self.root.mainloop()
        
if __name__ == "__main__":
    app = System()
    app.start()
