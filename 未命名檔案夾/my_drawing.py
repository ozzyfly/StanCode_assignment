"""
File: my_drawing.py
Name:Fei
----------------------
TODO: to draw a picture.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Drawing a picture
    """
    window = GWindow(width=800, height=500, title='MyFace')
    face = GOval(100, 150, x=300, y=50)
    window.add(face)
    face.filled = True
    face.fill_color = 'pink'
    hat = GOval(150, 50, x=280, y=30)
    window.add(hat)
    hat.filled = True
    cloth = GRect(200, 400, x=250, y=200)
    cloth.filled = True
    window.add(cloth)
    l_hand = GRect(50, 200, x=200, y=200)
    l_hand.filled = True
    window.add(l_hand)
    r_hand = GRect(50, 200, x=450, y=200)
    r_hand.filled = True
    window.add(r_hand)
    triangle0 = GPolygon()
    triangle0.add_vertex((350, 250))
    triangle0.add_vertex((400, 200))
    triangle0.add_vertex((300, 200))
    triangle0.filled = True
    triangle0.fill_color = "white"
    window.add(triangle0)
    apple = GOval(80, 80, x=310, y=95)
    window.add(apple)
    apple.filled = True
    apple.fill_color = "green"
    triangle = GPolygon()
    triangle.add_vertex((350, 220))
    triangle.add_vertex((370, 200))
    triangle.add_vertex((330, 200))
    triangle.filled = True
    triangle.fill_color = "tomato"
    window.add(triangle)
    tie = GRect(40, 250, x=330, y=220)
    tie.filled = True
    tie.fill_color = "tomato"
    window.add(tie)
    triangle2 = GPolygon()
    triangle2.add_vertex((350, 490))
    triangle2.add_vertex((370, 470))
    triangle2.add_vertex((330, 470))
    triangle2.filled = True
    triangle2.fill_color = "tomato"
    window.add(triangle2)
    lf = GOval(50, 50, x=200, y=400)
    window.add(lf)
    lf.filled = True
    lf.fill_color = "pink"
    rf = GOval(50, 50, x=450, y=400)
    window.add(rf)
    rf.filled = True
    rf.fill_color = "pink"
    triangle3 = GPolygon()
    triangle3.add_vertex((200, 200))
    triangle3.add_vertex((200, 240))
    triangle3.add_vertex((240, 200))
    triangle3.filled = True
    triangle3.fill_color = "white"
    triangle3.color = "white"
    window.add(triangle3)
    triangle4 = GPolygon()
    triangle4.add_vertex((460, 200))
    triangle4.add_vertex((500, 240))
    triangle4.add_vertex((500, 200))
    triangle4.filled = True
    triangle4.fill_color = "white"
    triangle4.color = "white"
    window.add(triangle4)
    top = GOval(80, 60, x=315, y=20)
    window.add(top)
    top.filled = True
    label = GLabel('The Son of Man')
    label.font = 'Courier-30-italic'
    window.add(label, 480, 50)


if __name__ == '__main__':
    main()
