import tkinter as tk
from tkinter import ttk, messagebox

from Controller.perfiles_controller import PerfilController


class PerfilView:
    def __init__(self, root):
        self.root = root
        self.root.title("App Móvil - Gestión de Perfiles")
        self.root.geometry("900x620")
        self.root.resizable(False, False)

        self.controlador = PerfilController()
        self.id_seleccionado = None

        self._crear_interfaz()
        self._cargar_perfiles()

    def _crear_interfaz(self):
        lbl_titulo = tk.Label(
            self.root,
            text="Administración de Perfiles Móviles",
            font=("Helvetica", 15, "bold"),
        )
        lbl_titulo.pack(pady=15)

        contenedor = tk.Frame(self.root)
        contenedor.pack(fill="both", expand=True, padx=20, pady=10)

        self._crear_formulario(contenedor)
        self._crear_tabla(contenedor)

    def _crear_formulario(self, contenedor):
        frame_form = tk.LabelFrame(
            contenedor,
            text=" Registrar Perfil ",
            font=("Helvetica", 10, "bold"),
        )
        frame_form.pack(side="left", fill="y", padx=(0, 15), ipadx=10, ipady=10)

        tk.Label(frame_form, text="Usuario:").pack(anchor="w", pady=(5, 2))
        self.entry_username = tk.Entry(frame_form, font=("Helvetica", 10), width=24)
        self.entry_username.pack(fill="x", pady=2)

        tk.Label(frame_form, text="Tipo de perfil:").pack(anchor="w", pady=(10, 2))
        self.combo_tipo = ttk.Combobox(
            frame_form,
            values=["Movil", "Pro"],
            state="readonly",
            width=22,
        )
        self.combo_tipo.current(0)
        self.combo_tipo.bind("<<ComboboxSelected>>", self._cambiar_tipo)
        self.combo_tipo.pack(fill="x", pady=2)

        tk.Label(frame_form, text="Meses de suscripción:").pack(anchor="w", pady=(10, 2))
        self.entry_meses = tk.Entry(frame_form, font=("Helvetica", 10), width=24)
        self.entry_meses.pack(fill="x", pady=2)
        self.entry_meses.config(state="disabled")

        btn_crear = tk.Button(
            frame_form,
            text="Crear perfil",
            bg="#4CAF50",
            fg="black",
            font=("Helvetica", 10, "bold"),
            command=self._crear_perfil,
        )
        btn_crear.pack(fill="x", pady=(20, 8))

        frame_acciones = tk.LabelFrame(
            frame_form,
            text=" Acciones del perfil ",
            font=("Helvetica", 10, "bold"),
        )
        frame_acciones.pack(fill="x", pady=(10, 0), ipadx=5, ipady=5)

        btn_ganar = tk.Button(
            frame_acciones,
            text="Ganar 10 gemas",
            command=lambda: self._operar_gemas("ganar"),
        )
        btn_ganar.pack(fill="x", pady=3)

        btn_gastar = tk.Button(
            frame_acciones,
            text="Gastar 10 gemas",
            command=lambda: self._operar_gemas("gastar"),
        )
        btn_gastar.pack(fill="x", pady=3)

        btn_offline = tk.Button(
            frame_acciones,
            text="Descargar contenido offline",
            command=self._descargar_offline,
        )
        btn_offline.pack(fill="x", pady=3)

        btn_eliminar = tk.Button(
            frame_acciones,
            text="Eliminar perfil",
            bg="#E53935",
            fg="white",
            command=self._eliminar_perfil,
        )
        btn_eliminar.pack(fill="x", pady=(12, 3))

        btn_recargar = tk.Button(
            frame_form,
            text="Recargar tabla",
            command=self._cargar_perfiles,
        )
        btn_recargar.pack(fill="x", pady=(15, 0))

    def _crear_tabla(self, contenedor):
        frame_tabla = tk.Frame(contenedor)
        frame_tabla.pack(side="right", fill="both", expand=True)

        scroll = ttk.Scrollbar(frame_tabla)
        scroll.pack(side="right", fill="y")

        columnas = ("ID", "Usuario", "Gemas", "Racha", "Notif.", "Meses", "Pro")
        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            yscrollcommand=scroll.set,
        )
        self.tabla.pack(fill="both", expand=True)
        scroll.config(command=self.tabla.yview)

        for columna in columnas:
            self.tabla.heading(columna, text=columna)

        self.tabla.column("ID", width=45, anchor="center")
        self.tabla.column("Usuario", width=150, anchor="w")
        self.tabla.column("Gemas", width=70, anchor="center")
        self.tabla.column("Racha", width=70, anchor="center")
        self.tabla.column("Notif.", width=70, anchor="center")
        self.tabla.column("Meses", width=70, anchor="center")
        self.tabla.column("Pro", width=60, anchor="center")

        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_perfil)

    def _cambiar_tipo(self, event=None):
        if self.combo_tipo.get() == "Pro":
            self.entry_meses.config(state="normal")
        else:
            self.entry_meses.delete(0, tk.END)
            self.entry_meses.config(state="disabled")

    def _cargar_perfiles(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for perfil in self.controlador.listar():
            self.tabla.insert(
                "",
                "end",
                iid=str(perfil["id_perfil"]),
                values=(
                    perfil["id_perfil"],
                    perfil["username"],
                    perfil["gemas"],
                    perfil["racha_dias"],
                    "Sí" if perfil["notificaciones_activas"] else "No",
                    perfil["meses_suscripcion"],
                    "Sí" if perfil["es_pro"] else "No",
                ),
            )

        self.id_seleccionado = None

    def _seleccionar_perfil(self, event=None):
        seleccion = self.tabla.selection()

        if seleccion:
            self.id_seleccionado = int(seleccion[0])

    def _crear_perfil(self):
        username = self.entry_username.get().strip()
        es_pro = self.combo_tipo.get() == "Pro"
        meses_texto = self.entry_meses.get().strip()

        meses = 0
        if es_pro:
            try:
                meses = int(meses_texto)
            except ValueError:
                messagebox.showerror(
                    "Error de formato",
                    "Los meses de suscripción deben ser un número entero.",
                )
                return

        exito, mensaje = self.controlador.crear(username, es_pro, meses)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.entry_username.delete(0, tk.END)
            self.entry_meses.delete(0, tk.END)
            self._cargar_perfiles()
        else:
            messagebox.showerror("Error", mensaje)

    def _validar_seleccion(self):
        if self.id_seleccionado is None:
            messagebox.showwarning(
                "Sin selección",
                "Selecciona un perfil de la tabla para realizar esta acción.",
            )
            return False
        return True

    def _operar_gemas(self, operacion):
        if not self._validar_seleccion():
            return

        if operacion == "ganar":
            exito, mensaje = self.controlador.ganar_gemas(self.id_seleccionado, 10)
        else:
            exito, mensaje = self.controlador.gastar_gemas(self.id_seleccionado, 10)

        if exito:
            messagebox.showinfo("Transacción exitosa", mensaje)
        else:
            messagebox.showerror("Transacción rechazada", mensaje)

        self._cargar_perfiles()

    def _descargar_offline(self):
        if not self._validar_seleccion():
            return

        exito, mensaje = self.controlador.descargar_offline(self.id_seleccionado)

        if exito:
            messagebox.showinfo("Descarga disponible", mensaje)
        else:
            messagebox.showerror("Descarga no disponible", mensaje)

        self._cargar_perfiles()

    def _eliminar_perfil(self):
        if not self._validar_seleccion():
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Deseas eliminar el perfil seleccionado?",
        )

        if not confirmar:
            return

        exito, mensaje = self.controlador.eliminar(self.id_seleccionado)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

        self._cargar_perfiles()
