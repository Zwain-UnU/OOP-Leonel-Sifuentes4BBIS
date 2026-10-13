import tkinter as tk
from tkinter import messagebox

from Models.login_model import User
from Views.home_view import DashboarVentana


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x380")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):
        lbl_titulo = tk.Label(
            self.root,
            text="Iniciar Sesión",
            font=("Helvetica", 16, "bold")
        )
        lbl_titulo.pack(pady=25)

        lbl_usuario = tk.Label(
            self.root,
            text="Usuario:",
            font=("Helvetica", 10)
        )
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))

        self.entry_usuario = tk.Entry(
            self.root,
            font=("Helvetica", 11)
        )
        self.entry_usuario.pack(fill="x", padx=30)

        lbl_pass = tk.Label(
            self.root,
            text="Contraseña:",
            font=("Helvetica", 10)
        )
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))

        self.entry_pass = tk.Entry(
            self.root,
            font=("Helvetica", 11),
            show="*"
        )
        self.entry_pass.pack(fill="x", padx=30)

        btn_ingresar = tk.Button(
            self.root,
            text="Entrar",
            font=("Helvetica", 11, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2",
            command=self.validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=30)

    def validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning(
                "Campos vacíos",
                "Por favor ingresa usuario y contraseña.",
                parent=self.root
            )
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario:
            nombre = datos_usuario[0]["nombre"]

            messagebox.showinfo(
                "Bienvenido",
                f"¡Hola {nombre}! Acceso concedido.",
                parent=self.root
            )

            self.abrir_dashboard(nombre)
        else:
            messagebox.showerror(
                "Error de acceso",
                "Usuario o contraseña incorrectos.",
                parent=self.root
            )

    def abrir_dashboard(self, nombre_completo):
        self.root.destroy()

        root_dashboard = tk.Tk()
        DashboarVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()
