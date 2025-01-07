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

        left_line = Line(top_left, bottom_left)
        right_line = Line(top_right, bottom_right)
        top_line = Line(top_left, top_right)
        bottom_line = Line(bottom_left, bottom_right)

        left_color = "black" if self.has_left_wall else "#d9d9d9"
        right_color = "black" if self.has_right_wall else "#d9d9d9"
        top_color = "black" if self.has_top_wall else "#d9d9d9"
        bottom_color = "black" if self.has_bottom_wall else "#d9d9d9"

        left_line.draw(self._win.canvas, color=left_color)
        right_line.draw(self._win.canvas, color=right_color)
        top_line.draw(self._win.canvas, color=top_color)
        bottom_line.draw(self._win.canvas, color=bottom_color)

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
        self._break_entrance_and_exit()

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
                self._draw_cell(cell)

            self._cells.append(col)
 
    def _draw_cell(self,cell):
        if self._win:
            cell.draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        tl_cell = self._cells[0][0]
        br_cell = self._cells[-1][-1]

        tl_cell.has_top_wall = False
        br_cell.has_bottom_wall = False

        self._draw_cell(tl_cell)
        self._draw_cell(br_cell)