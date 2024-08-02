import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen

# importamos las librerías necesarias para el programa

"""
    Realiza una serie de cuadrados en una ventana.

    Parámetros:
    self : representa la instancia de la clase actual,permite acceder
        a los métodos de la clase.
    root:ventana principal de la aplicación Tkinter
    self.canvas.pack(fill=tk.BOTH, expand=True):determina cómo la ventana
        se expandirá para llenar el espacio disponible dentro de su contenedor

    Retorna:
    Una cuadrícula de rectángulos establecida en una ventana nueva.

    Objetivo de la función: dibujar una cuadrícula de rectángulos con
    la capacidad de ser alterada y establecer cualquier clase de formato de
    hoja rayada.
    """


class DiagramDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagram Drawer with Tkinter and Turtle")

        # Crear un lienzo de desplazamiento para la tortuga
        self.canvas = ScrolledCanvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Crear la pantalla de la tortuga
        self.screen = TurtleScreen(self.canvas)
        self.screen.bgcolor("white")

        # Crear una tortuga
        self.turtle = RawTurtle(self.screen)
        self.turtle.speed(0)  # Velocidad máxima

        # Dibujar los recuadros
        self.draw_rectangles()

    # Define el tamaño de cada cuadrícula
    def draw_rectangles(self):
        self.turtle.penup()
        self.turtle.goto(-100, 100)
        self.turtle.pendown()

        # Dibujar una cuadrícula de recuadros
        for i in range(4):
            for j in range(4):
                self.draw_rectangle(-100 + j * 50, 100 - i * 50)

    # Establece la próxima posición en la que comenzará el próximo rectángulo
    def draw_rectangle(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

        # Dibujar un recuadro de 100x100 píxeles
        for _ in range(4):
            self.turtle.forward(50)
            self.turtle.right(90)


'''Convención en Python que se utiliza para ejecutar código solo
    cuando el script se ejecuta directamente, con el objetivo de
    controlar la ejecución del código.'''
if __name__ == "__main__":
    root = tk.Tk()
    app = DiagramDrawer(root)
    root.mainloop()
