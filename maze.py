from graphics import Window, Point, Line
import time


class Cell():
    def __init__(self,x1,x2,y1,y2,window:Window,
                 has_left_wall=True, has_right_wall=True,
                 has_top_wall=True, has_bottom_wall=True,
                 ):
        self._x1 = min(x1, x2)
        self._x2 = max(x1, x2)
        self._y1 = min(y1, y2)
        self._y2 = max(y1, y2)
        self._win = window
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.center = Point( (self._x1 + self._x2)/2,
                                (self._y1 + self._y2)/2)

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            left_line = Line(top_left, bottom_left)
            left_line.draw(self._win.canvas, color="black")

        if self.has_right_wall:
            right_line = Line(top_right, bottom_right)
            right_line.draw(self._win.canvas, color="black")

        if self.has_top_wall:
            top_line = Line(top_left, top_right)
            top_line.draw(self._win.canvas, color="black")

        if self.has_bottom_wall:
            bottom_line = Line(bottom_left, bottom_right)
            bottom_line.draw(self._win.canvas, color="black")

    def draw_move(self, to_cell, undo=False):
            color = "gray" if undo else "red"
            origin = to_cell if undo else self
            dest = self if undo else to_cell
            
            line = Line(origin.center, dest.center)
            line.draw(self._win.canvas,color)


    def __repr__(self):
        return f"""x1: {self._x1}, x2: {self._x2},
y1: {self._y1}, y2: {self._y2},
        {self.has_top_wall}
{self.has_left_wall}   {self.center}     {self.has_right_wall}
        {self.has_bottom_wall}"""
    

class Maze():
    def __init__(self, x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win=None):  
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                x = self._x1 + j*self._cell_size_x
                y = self._y1 + i*self._cell_size_y
                cell = Cell(x, x + self._cell_size_x, 
                            y, y +self._cell_size_y,
                            self._win)
                col.append(cell)
                if self._win:
                    cell.draw()
                    self._animate()

            self._cells.append(col)
 
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)