from graphics import Window, Point, Line


class Cell():
    def __init__(self,x1,x2,y1,y2,window= Window,
                 has_left_wall=False, has_right_wall=False,
                 has_top_wall=False, has_bottom_wall=False,
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



    def __repr__(self):
        return f"""x1: {self._x1}, x2: {self._x2},
y1: {self._y1}, y2: {self._y2},
        {self.has_top_wall}
{self.has_left_wall}        {self.has_right_wall}
        {self.has_bottom_wall}"""