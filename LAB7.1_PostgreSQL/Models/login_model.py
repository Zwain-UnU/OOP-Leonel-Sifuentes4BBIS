from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw 
        self.db = Database_connection()

    def auth(self):
            # 1. Primero, le pedimos a Python que imprima ABSOLUTAMENTE TODO lo que hay en la tabla
            query_prueba = "SELECT * FROM login_system_db.users"
            todos_los_usuarios = self.db.ejecutar_consulta(query_prueba)
            print(f"\n--- LO QUE PYTHON VE EN LA BD ---")
            print(todos_los_usuarios)
            print("---------------------------------\n")

            # 2. Tu consulta normal
            query = "SELECT * FROM login_system_db.users WHERE username = %s AND passw = %s"
            result = self.db.ejecutar_consulta(query, (self.username, self.password))
            
            print(f"Intento con -> Usuario: '{self.username}', Clave: '{self.password}'")
            print(f"Resultado de coincidencia: {result}")
            
            return result