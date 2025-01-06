from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        self.__is_running = False

    def draw_line(self,line=Line, color=str):
        line.draw(canvas=self.canvas,color=color)


class Line():
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas=Canvas, color=str):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=color, width=2
        )


class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y