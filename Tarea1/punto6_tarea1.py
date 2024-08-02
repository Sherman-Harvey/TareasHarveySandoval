import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen

# importamos las librerías necesarias para el programa


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

    def draw_rectangles(self):
        self.turtle.penup()
        self.turtle.goto(-100, 100)
        self.turtle.pendown()

        # Dibujar una cuadrícula de recuadros
        for i in range(4):
            for j in range(4):
                self.draw_rectangle(-100 + j * 50, 100 - i * 50)

    def draw_rectangle(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

        # Dibujar un recuadro de 100x100 píxeles
        for _ in range(4):
            self.turtle.forward(50)
            self.turtle.right(90)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiagramDrawer(root)
    root.mainloop()
