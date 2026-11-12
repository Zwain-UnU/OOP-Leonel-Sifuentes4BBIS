from tkinter import Tk 
from Views.login_view_3 import LoginView
class System:
    def __init__(self):
        self.root = Tk()

    def start(self):
        self.root = Tk()
        LoginView(self.root)
        self.root.mainloop()
        




if __name__ == "__main__":
    app = System()
    app.start()
