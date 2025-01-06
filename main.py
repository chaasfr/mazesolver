from graphics import Window, Line, Point

def draw_lines(win=Window):
    p1 = Point(400,200)
    p2 = Point(400,400)

    p3 = Point(300, 300)
    p4 = Point(500, 300)

    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    win.draw_line(line1, color="blue")
    win.draw_line(line2, color="red")

def main():
   win = Window(800, 600)
   draw_lines(win)
   win.wait_for_close() 

if __name__ == "__main__":
    main()