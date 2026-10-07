import tkinter as tk
from tkinter import ttk
import os 
from abc import ABC, abstractmethod 

class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class SmartSpeakers(SmartDevice):
    def __init__(self):
        super().__init__("Echo Dot 5") #PARA HEREDAR EL ATRIBUTO DE LA CLASE PADRE DE ARRIBA SE PONE SUPER

    def turn_on(self):
        return f"{self.name}, is playing Lofi music at volume 20%"   

    def turn_off(self):
            return f"{self.name}, off"    

class SmartWatch(SmartDevice):
    def __init__(self):
        super().__init__("SmarWatch de charly kirky")

    def turn_on(self):
        return f"{self.name}, is watching that the hour is 08:00 p.m"

    def turn_off(self):
            return f"{self.name}, off"

class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("AC LAB 2")

    def turn_on(self):
            return f"{self.name}, is colder"

    def turn_off(self):
            return f"{self.name}, off"
     
     

class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. Window Settings --- 
        self.title("Lab6: Polymorphism with GUI")
        self.geometry("600x500")
        self .resizable(False, False)


        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "images/home.png")

        if os.path.exists(icon_path):
            self.app_icon = tk.PhotoImage(file=icon_path)
            self.iconphoto(True, self.app_icon)
        else:
            print(f"The icon file doesn't exists: {icon_path}")


        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "Speaker": SmartSpeakers(),
            "Watch": SmartWatch(),
            "AC": SmartAC()
        }


        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="Smart Home Center",
            font=("Arial", 30, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)



        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Arial", 20, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)



        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)



        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)



        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="Turn On Device",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 15, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        btn_actionoff = tk.Button(
            self,
            text="Turn Off Device",
            command=self.turn_off_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 15, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_actionoff.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)


        log_frame = tk.LabelFrame(self, text=" Activity Log ", font=("Arial", 11, "bold"))
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.log_list = tk.Listbox(log_frame, height=5, font=("Consolas", 10))
        self.log_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(log_frame, command=self.log_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_list.config(yscrollcommand=scrollbar.set)



    def _handle_action(self):
        # 1. Obtener la llave actual
        chosen_key = self.selected_key.get()

        active_object: SmartDevice = self.items[chosen_key]

        result_message = active_object.turn_on()

        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        
        self.log_list.insert(tk.END, f"[ON] {result_message}")
        self.log_list.yview(tk.END)
       
    def turn_off_action(self):
        chosen_key = self.selected_key.get()

        active_object: SmartDevice = self.items[chosen_key]

        result_message = active_object.turn_off()

        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))

        self.log_list.insert(tk.END, f"[OFF] {result_message}")
        self.log_list.yview(tk.END)



# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
