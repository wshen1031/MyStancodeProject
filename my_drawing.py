"""
File: 
Name: Willy
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Basketball never stop

    I love to play basketball. This is a picture of me shooting a three. I first think of a basketball because it should
    be easy to create.
    """
    window = GWindow(width=600, height=800, title='basketball never stop')
    court = GPolygon()
    court.add_vertex((0, window.height))
    court.add_vertex((0, 600))
    court.add_vertex((200, 350))
    court.add_vertex((window.width, 350))
    court.add_vertex((window.width, window.height))
    court.filled = True
    court.fill_color = 'sandybrown'
    window.add(court)
    pillar = GRect(30, 300, x=400, y=150)
    pillar.filled = True
    pillar.fill_color = 'blue'
    window.add(pillar)
    backboard = GRect(250, 150, x=285, y=50)
    backboard.filled = True
    backboard.fill_color = 'white'
    window.add(backboard)
    red_line = GRect(150, 80)
    red_line.filled = True
    red_line.fill_color = 'darkred'
    window.add(red_line, x=340, y=100)
    rec = GRect(130, 60)
    rec.filled = True
    rec.fill_color = 'white'
    window.add(rec, x=350, y=110)
    rim = GRect(70, 10)
    rim.filled = True
    rim.fill_color = 'red'
    window.add(rim, x=380, y=160)
    net = GLine(380, 170, 390, 230)
    net_1 = GLine(450, 170, 440, 230)
    net_2 = GLine(395, 170, 395, 230)
    net_3 = GLine(410, 170, 410, 230)
    net_4 = GLine(425, 170, 425, 230)
    net_5 = GLine(435, 170, 435, 230)
    net_6 = GLine(385, 185, 445, 185)
    net_7 = GLine(387, 210, 447, 210)
    window.add(net)
    window.add(net_1)
    window.add(net_2)
    window.add(net_3)
    window.add(net_4)
    window.add(net_5)
    window.add(net_6)
    window.add(net_7)
    leftarm = GRect(15, 90, x=190, y=490)
    leftarm.filled = True
    leftarm.fill_color = 'tan'
    window.add(leftarm)
    rightarm = GRect(15, 90, x=210, y=490)
    rightarm.filled = True
    rightarm.fill_color = 'tan'
    window.add(rightarm)
    lefthand = GPolygon()
    lefthand.add_vertex((190, 480))
    lefthand.add_vertex((200, 490))
    lefthand.add_vertex((218, 475))
    lefthand.add_vertex((208, 465))
    lefthand.filled = True
    lefthand.fill_color = 'tan'
    window.add(lefthand)
    righthand = GArc(25, 50, 0, 180)
    righthand.filled = True
    righthand.fill_color = 'tan'
    window.add(righthand, x=215, y=475)
    head = GOval(75, 75, x=120, y=500)
    head.filled = True
    head.fill_color = 'tan'
    window.add(head)
    neck = GRect(15, 10, x=150, y=575)
    neck.filled = True
    neck.fill_color = 'tan'
    window.add(neck)
    body = GRect(95, 170, x=110, y=585)
    body.filled = True
    body.fill_color = 'darkgreen'
    window.add(body)
    leg_1 = GRect(15, 30, x=125, y=760)
    leg_1.filled = True
    leg_1.fill_color = 'tan'
    window.add(leg_1)
    leg_2 = GRect(15, 30, x=170, y=760)
    leg_2.filled = True
    leg_2.fill_color = 'tan'
    window.add(leg_2)
    basketball = GOval(80, 80, x=250, y=400)
    basketball.filled = True
    basketball.fill_color = 'maroon'
    window.add(basketball)
    line = GLine(290, 400, 290, 480)
    window.add(line)
    line_1 = GArc(80, 60, 280, 160)
    window.add(line_1, x=248, y=408)
    line_2 = GArc(80, 60, 100, 160)
    window.add(line_2, x=300, y=408)
    line_3 = GLine(250, 440, 330, 440)
    window.add(line_3)





if __name__ == '__main__':
    main()
