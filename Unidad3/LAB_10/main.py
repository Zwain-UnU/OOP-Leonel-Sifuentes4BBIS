import tkinter as tk

from Views.perfil_view import PerfilView


def main():
    root = tk.Tk()
    PerfilView(root)
    root.mainloop()


if __name__ == "__main__":
    main()
