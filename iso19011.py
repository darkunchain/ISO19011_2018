import tkinter as tk

class MapaMental:
    def __init__(self, root):
        self.root = root
        self.root.title("Mapa Mental Interactivo")
        self.current_level = 0  # Nivel actual del mapa mental
        self.history = []  # Historial de niveles para poder retroceder

        # Estructura del mapa mental (puedes modificarla según tus necesidades)
        self.conceptos = {
            0: [
                {"titulo": "Concepto A", "texto": "Explicación del Concepto A", "subnivel": 1},
                {"titulo": "Concepto B", "texto": "Explicación del Concepto B", "subnivel": 2},
                {"titulo": "Concepto C", "texto": "Explicación del Concepto C", "subnivel": 3}
            ],
            1: [
                {"titulo": "Subconcepto A1", "texto": "Explicación del Subconcepto A1", "subnivel": None},
                {"titulo": "Subconcepto A2", "texto": "Explicación del Subconcepto A2", "subnivel": None}
            ],
            2: [
                {"titulo": "Subconcepto B1", "texto": "Explicación del Subconcepto B1", "subnivel": None},
                {"titulo": "Subconcepto B2", "texto": "Explicación del Subconcepto B2", "subnivel": None}
            ],
            3: [
                {"titulo": "Subconcepto C1", "texto": "Explicación del Subconcepto C1", "subnivel": None},
                {"titulo": "Subconcepto C2", "texto": "Explicación del Subconcepto C2", "subnivel": None}
            ]
        }

        self.botones = []  # Almacena los botones de los conceptos
        self.label_explicacion = None  # Etiqueta para mostrar el texto explicativo
        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la interfaz gráfica según el nivel actual."""
        self.limpiar_interfaz()

        # Mostrar los conceptos del nivel actual
        for i, concepto in enumerate(self.conceptos[self.current_level]):
            boton = tk.Button(
                self.root,
                text=concepto["titulo"],
                command=lambda c=concepto: self.seleccionar_concepto(c)
            )
            boton.grid(row=0, column=i, padx=10, pady=10)
            self.botones.append(boton)

        # Botón "Atrás" para volver al nivel anterior
        if self.history:  # Solo mostrar el botón si hay un nivel anterior
            boton_atras = tk.Button(self.root, text="Atrás", command=self.volver_atras)
            boton_atras.grid(row=1, column=0, columnspan=len(self.conceptos[self.current_level]), pady=10)

    def seleccionar_concepto(self, concepto):
        """Maneja la selección de un concepto."""
        if self.label_explicacion:
            self.label_explicacion.destroy()  # Limpia la explicación anterior

        # Mostrar el texto explicativo del concepto seleccionado
        self.label_explicacion = tk.Label(self.root, text=concepto["texto"], wraplength=400)
        self.label_explicacion.grid(row=2, column=0, columnspan=len(self.conceptos[self.current_level]), pady=10)

        # Navegar al subnivel si existe
        if concepto["subnivel"] is not None:
            self.history.append(self.current_level)  # Guardar el nivel actual en el historial
            self.current_level = concepto["subnivel"]  # Cambiar al subnivel
            self.crear_interfaz()  # Actualizar la interfaz

    def volver_atras(self):
        """Vuelve al nivel anterior."""
        if self.history:  # Si hay un nivel anterior en el historial
            self.current_level = self.history.pop()  # Recuperar el nivel anterior
            self.crear_interfaz()  # Actualizar la interfaz

    def limpiar_interfaz(self):
        """Limpia la interfaz gráfica actual."""
        for boton in self.botones:
            boton.destroy()
        self.botones = []
        if self.label_explicacion:
            self.label_explicacion.destroy()
            self.label_explicacion = None

if __name__ == "__main__":
    root = tk.Tk()
    app = MapaMental(root)
    root.mainloop()