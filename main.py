from graphics import Window, Line, Point
from maze import Cell

def draw_lines(win=Window):
    p1 = Point(400,200)
    p2 = Point(400,400)

    p3 = Point(300, 300)
    p4 = Point(500, 300)

    p5 = Point(50,50)
    p6 = Point(450, 50)

    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    line3 = Line(p5, p6)

    win.draw_line(line1, color="blue")
    win.draw_line(line2, color="red")
    win.draw_line(line3, color="black")

def draw_cells(win=Window):
   x_min = 50
   x_max = 750
   y_min = 50
   y_max = 550
   space = 25
   cell_width = 50
   cell_height = 50
   i = 0
   row = 0
   col = 0
   x2= cell_width
   y2 = cell_height
   while i < 16 and ( x2 <= x_max or y2 <= y_max):
       x1 = x_min + col * (cell_width + space)
       x2 = x1 + cell_width
       y1 = y_min + row * (cell_height + space)
       y2 = y1 + cell_height

       # convert i into 4-digit bin. e;g; 14 -> 1110 so we can use each digit as a bool for a wall
       i_bin = bin(i)[2:].zfill(4) 
       has_top_wall = i_bin[0] == '1'
       has_left_wall = i_bin[1] == '1'
       has_right_wall = i_bin[2] == '1'
       has_bottom_wall = i_bin[3] == '1'

       cell = Cell(x1, x2, y1, y2, win,
                   has_left_wall=has_left_wall,
                   has_right_wall=has_right_wall,
                   has_bottom_wall=has_bottom_wall,
                   has_top_wall=has_top_wall)
       print(cell)
       cell.draw()
       i += 1
       if x_max - x2 > cell_width + space:
           col += 1
       else:
           col = 1
           row += 1



def main():
   win = Window(800, 600)
   #draw_lines(win)
   draw_cells(win)
   win.wait_for_close() 

if __name__ == "__main__":
    main()